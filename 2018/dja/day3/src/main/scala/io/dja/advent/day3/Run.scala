package io.dja.advent.day3

import scala.io.Source

object Run extends App {

  // TODO: make a common library
  val data = loadData(args(0))

  val claimRegex = """#(\d+)\s@\s(\d+,\d+):\s(\d+x\d+)""".r

  var claimGrid = Array.ofDim[Int](15, 15)
  data.foreach { d =>
    val claimData: Array[String] = d match {
      case claimRegex(claimNumber, claimCoordinates, claimDimensions) => Array[String](claimNumber, claimCoordinates, claimDimensions)
    }
    val parsedClaimDimensions: Array[Int] = claimData(2).split("x").map(_.toInt)
    val parsedClaimCoords: Array[Int] = claimData(1).split(",").map(_.toInt)
    val claimXStart: Int = parsedClaimCoords(0)
    val claimYStart: Int = parsedClaimCoords(1)
    val claimXDim: Int = parsedClaimDimensions(0)
    val claimYDim: Int = parsedClaimDimensions(1)
    val claimNumber: Int = claimData(0).toInt
    for (i <- claimXStart until claimXStart + claimXDim) {
      for (j <- claimYStart until claimYStart + claimYDim) {
        claimGrid(i)(j) = claimNumber
      }
    }
  }

  print(claimGrid.map(_.mkString).mkString("\n"))
  def loadData(path: String): List[String] = {
    Source.fromFile(path)
      .getLines().toList
  }

}
