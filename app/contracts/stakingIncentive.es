{
    val emissionContractHash = _emissionContractHash
    val stakeStateContractHash = _stakeStateContractHash
    val stakeTokenID = _stakeTokenID

    //Emit transaction
    if (blake2b256(INPUTS(0).propositionBytes) == stakeStateContractHash && blake2b256(INPUTS(2).propositionBytes) == emissionContractHash)
    {
        sigmaProp(allOf(Coll(
            INPUTS(INPUTS.size-1).id == SELF.id,
            OUTPUTS(3).propositionBytes == SELF.propositionBytes,
            OUTPUTS(3).value >= SELF.value - 4000000,
            OUTPUTS(4).value == 3000000
        )))
    }
    else
    {
        //Compound transaction
        if (blake2b256(INPUTS(0).propositionBytes) == emissionContractHash)
        {
            val stakeBoxes = INPUTS.filter({(box: Box) => if (box.tokens.size > 0) box.tokens(0)._1 == stakeTokenID && box.R4[Coll[Long]].get(0) == INPUTS(0).R4[Coll[Long]].get(1) else false}).size
            val txValue = 900000 + 750000 * stakeBoxes
            val minerFee = 1000000 + 500000 * stakeBoxes
            sigmaProp(allOf(Coll(
                INPUTS(INPUTS.size-1).id == SELF.id,
                OUTPUTS(INPUTS.size-1).propositionBytes == SELF.propositionBytes,
                OUTPUTS(INPUTS.size-1).value >= SELF.value - txValue,
                OUTPUTS(INPUTS.size).value == txValue - minerFee,
                OUTPUTS(INPUTS.size+1).value == minerFee,
                INPUTS.size == stakeBoxes + 2
            )))
        }
        else
        {
            //Dust consolidation tx
            if (OUTPUTS.size == 3)
            {
                val dustBoxes = INPUTS.filter({(box: Box) => box.propositionBytes == SELF.propositionBytes}).size
                val reward = 500000 * dustBoxes
                sigmaProp(allOf(Coll(
                    OUTPUTS(0).propositionBytes == SELF.propositionBytes,
                    OUTPUTS(0).value > SELF.value,
                    SELF.value <= 100000000,
                    OUTPUTS(1).value == reward,
                    OUTPUTS(2).value == 1000000
                )))
            }
            else
            {
                sigmaProp(false)
            }
        }
    }
}