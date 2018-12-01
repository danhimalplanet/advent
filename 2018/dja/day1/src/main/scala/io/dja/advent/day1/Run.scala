package io.dja.advent.day1

import java.util

import scala.io.Source

object Run {

  var seen: util.HashMap[Int, Int] = new util.HashMap[Int, Int]
  val data = loadData()

  def main(args: Array[String]): Unit = {
    partOne()
  }

  def partOne(): Unit = println(s"part 1 result: ${data.sum}")

  def loadData(): Array[Int] =
    Source.fromResource("input").getLines.map(_.replace("+","").toInt).toArray

}

