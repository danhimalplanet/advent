package io.dja.advent.day1

import scala.io.Source

object Run {
  def main(args: Array[String]): Unit = {
    val lines: Iterator[String] = Source.fromResource("input").getLines
    while (lines.hasNext) {
      println(lines.next)
    }
  }
}

