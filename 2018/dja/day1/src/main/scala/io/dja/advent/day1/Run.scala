package io.dja.advent.day1

import scala.io.Source

object Run {
  def main(args: Array[String]): Unit = {
    partOne()
  }

  def partOne(): Unit = {
    val lines: Iterator[String] = Source.fromResource("input").getLines
    var result: Int = 0

    while (lines.hasNext) {
      val next = lines.next.replace("+", "")
      result += next.toInt
    }
    println(s"part 1 result: ${result}")
  }
}

