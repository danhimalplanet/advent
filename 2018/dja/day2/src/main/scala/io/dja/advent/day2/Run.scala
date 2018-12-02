package io.dja.advent.day2


import scala.collection.immutable.HashMap
import scala.io.Source

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

  def markComplete(count: Int, line: String): Unit = {
    seen += (s"${line}${count}" -> count)
  }
  def loadData(file: String): List[String] = {
    Source.fromFile(file)
      .getLines()
      .toList
  }
}
