#!/usr/bin/env nextflow

nextflow.enable.dsl=2

workflow {
    inputString = params.inputString

    processToUpper(inputString) | view
}

process processToUpper {
    input:
    val inputString

    output:
    val result

    script:
    result = inputString.toUpperCase()
    """
    echo $result
    """
}

