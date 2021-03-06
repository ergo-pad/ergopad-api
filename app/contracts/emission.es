{{
      // Emission
      // Registers:
      // 4:0 Long: Total amount staked
      // 4:1 Long: Checkpoint
      // 4:2 Long: Stakers
      // 4:3 Long: Emission amount
      // Assets:
      // 0: Emission NFT: Identifier for emit box
      // 1: Staked Tokens (ErgoPad): Tokens to be distributed

      val stakeStateNFT = fromBase64("{stakeStateNFT}")
      val stakeTokenID = fromBase64("{stakeTokenID}")
      val stakedTokenID = fromBase64("{stakedTokenID}")
      val stakeStateInput = INPUTS(0).tokens(0)._1 == stakeStateNFT

      if (stakeStateInput && INPUTS(2).id == SELF.id) {{ // Emit transaction
          val remainingAndDust = INPUTS(1).tokens(1)._2 + (if (SELF.tokens.size >= 2) SELF.tokens(1)._2 else 0L)
          sigmaProp(allOf(Coll(
              //Stake State, Stake Pool, Emission (self) => Stake State, Stake Pool, Emission
              OUTPUTS(2).propositionBytes == SELF.propositionBytes,
              OUTPUTS(2).R4[Coll[Long]].get(0) == INPUTS(0).R4[Coll[Long]].get(0),
              OUTPUTS(2).R4[Coll[Long]].get(1) == INPUTS(0).R4[Coll[Long]].get(1),
              OUTPUTS(2).R4[Coll[Long]].get(2) == INPUTS(0).R4[Coll[Long]].get(2),
              OUTPUTS(2).R4[Coll[Long]].get(3) == (if (INPUTS(1).R4[Coll[Long]].get(0) < remainingAndDust) INPUTS(1).R4[Coll[Long]].get(0) else remainingAndDust),
              OUTPUTS(2).tokens(0)._1 == SELF.tokens(0)._1,
              OUTPUTS(2).tokens(1)._1 == stakedTokenID,
              OUTPUTS(2).tokens(1)._2 == OUTPUTS(2).R4[Coll[Long]].get(3)
          )))
      }} else {{
      if (INPUTS(0).id == SELF.id) {{ // Compound transaction
          // Emission (SELF), Stake*N => Emission, Stake*N
          val stakeBoxes = INPUTS.filter({{(box: Box) => if (box.tokens.size > 0) box.tokens(0)._1 == stakeTokenID && box.R4[Coll[Long]].get(0) == SELF.R4[Coll[Long]].get(1) else false}})
          val rewardsSum = stakeBoxes.fold(0L, {{(z: Long, box: Box) => z+(box.tokens(1)._2*SELF.R4[Coll[Long]].get(3)/SELF.R4[Coll[Long]].get(0))}})
          val remainingTokens = if (SELF.tokens(1)._2 <= rewardsSum) OUTPUTS(0).tokens.size == 1 else (OUTPUTS(0).tokens(1)._1 == stakedTokenID && OUTPUTS(0).tokens(1)._2 >= (SELF.tokens(1)._2 - rewardsSum))
          sigmaProp(allOf(Coll(
               OUTPUTS(0).propositionBytes == SELF.propositionBytes,
               OUTPUTS(0).tokens(0)._1 == SELF.tokens(0)._1,
               remainingTokens,
               OUTPUTS(0).R4[Coll[Long]].get(0) == SELF.R4[Coll[Long]].get(0),
               OUTPUTS(0).R4[Coll[Long]].get(1) == SELF.R4[Coll[Long]].get(1),
               OUTPUTS(0).R4[Coll[Long]].get(2) == SELF.R4[Coll[Long]].get(2) - stakeBoxes.size,
               OUTPUTS(0).R4[Coll[Long]].get(3) == SELF.R4[Coll[Long]].get(3)
           )))
      }} else {{
          sigmaProp(false)
      }}
      }}
  }}