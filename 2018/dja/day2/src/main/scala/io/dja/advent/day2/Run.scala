package io.dja.advent.day2


import scala.collection.immutable.HashMap
import scala.collection.mutable.ListBuffer
import scala.io.Source
import scala.util.control.Breaks._

object Run extends App {

  val data = loadData(args(0))
  var seen: HashMap[String, Int] = new HashMap[String, Int]()

  for (line <- data) {
    line.toCharArray.foreach { character =>
      var threes: Int = 0
      var twos: Int = 0
      line.count(_ == character) match {
        case 1 => println(s"skipping")
        case 2 => markComplete(2, line)
        case 3 => markComplete(3, line)
      }

    }
  }

  var twos: Int = 0
  var threes: Int = 0
  seen.foreach { case (k, v) =>
    v match {
      case 2 => twos += 1
      case 3 => threes += 1
    }

  }
  println(s"Part 1 result: ${twos * threes}")

  val keys = seen.keys.map(_.dropRight(1)).toList

  part2()
  def isOffByOne(first: String, second: String): Int = {
    var iterator = 0
    var different = new ListBuffer[Int]
    val firstChars = first.toCharArray
    val secondChars = second.toCharArray
    while (iterator < first.length) {
      if (firstChars(iterator) != secondChars(iterator)) {
        different += iterator
      }
      if (different.length > 1) {
        return 0
      }
      iterator += 1
    }
    if (different.length == 0) {
      return 0
    }
    return different(0)
  }

  def part2(): Unit = {
    breakable {
      for (i <- keys) {
        for (j <- keys) {
          val result = isOffByOne(i, j)
          if (result != 0) {
            val iChars = i.toCharArray
            println(s"Part 2 ${iChars.slice(0, result).mkString}${iChars.drop(result +1).mkString}")
            break
          }
        }
      }
    }
  }

  def markComplete(count: Int, line: String): Unit = {
    seen += (s"${line}${count}" -> count)
  }

  def loadData(file: String): List[String] = {
    Source.fromFile(file)
      .getLines()
      .toList
  }
}
