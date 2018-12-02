package io.dja.advent.day2

import scala.io.Source

object Run extends App {

  val data = loadData(args(0))
  println(s"DATA ${data}")
  def loadData(file: String): List[String] = {
    Source.fromFile(file)
      .getLines()
      .toList
  }


}
