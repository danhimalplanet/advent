package io.dja.advent.day3

import java.util

import scala.io.Source
import scala.util.control.Breaks._

object Run extends App {

  // TODO: make a common library
  val data = loadData(args(0))

  val claimRegex = """#(\d+)\s@\s(\d+,\d+):\s(\d+x\d+)""".r

  var claimGrid = Array.ofDim[String](1000, 1000)
  //                                                    claimNumber -> [ 0: claimXStart
  //                                                                     1: claimYStart
  //                                                                     2: claimXDim
  //                                                                     3: claimYDim ]
  var parsedClaimCoordinatesAndDimensions: util.HashMap[String, Array[Int]] = new util.HashMap
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
    val claimNumber: String = claimData(0)
    parsedClaimCoordinatesAndDimensions.put(claimNumber, Array(parsedClaimCoords, parsedClaimDimensions).flatten)
    for (i <- claimXStart until claimXStart + claimXDim) {
      for (j <- claimYStart until claimYStart + claimYDim) {
        claimGrid(i)(j) = claimNumber
      }
    }
  }

  val iterator = parsedClaimCoordinatesAndDimensions.entrySet().iterator()
  while(iterator.hasNext) {
    val pair = iterator.next()
    val claimNumber = pair.getKey
    val claimData = pair.getValue
    val claimXStart = claimData(0)
    val claimYStart = claimData(1)
    val claimXDim = claimData(2)
    val claimYDim = claimData(3)
    for (i <- claimXStart until claimXStart + claimXDim) {
      for (j <- claimYStart until claimYStart + claimYDim) {
        if (claimGrid(i)(j) != claimNumber) {
          claimGrid(i)(j) = "X"
        }
      }
    }
  }

  var overlapping: Int = claimGrid.flatten.count(_ == "X")
  var wholeClaimId: Int = 0
  val iterator2 = parsedClaimCoordinatesAndDimensions.entrySet().iterator()
  while(iterator2.hasNext) {
    val pair = iterator2.next()
    val claimNumber = pair.getKey
    val claimData = pair.getValue
    val claimXStart = claimData(0)
    val claimYStart = claimData(1)
    val claimXDim = claimData(2)
    val claimYDim = claimData(3)
    breakable {
      for (i <- claimXStart until claimXStart + claimXDim) {
        for (j <- claimYStart until claimYStart + claimYDim) {
          if (claimGrid(i)(j) == "X") {
            break
          }
        }
      }
      wholeClaimId = claimNumber.toInt
    }
  }

  println(s"Part 1: ${overlapping}")
  println(s"Part 2: ${wholeClaimId}")

  def loadData(path: String): List[String] = {
    Source.fromFile(path)
      .getLines().toList
  }

}
