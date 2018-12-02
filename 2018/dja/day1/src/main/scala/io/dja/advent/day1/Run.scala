package io.dja.advent.day1

import java.util

import scala.collection.mutable.ListBuffer
import scala.io.Source
import scala.util.control.Breaks._

object Run {

  var seen: ListBuffer[Int] = new ListBuffer[Int]
  var result: Int = _

  def main(args: Array[String]): Unit = {
    val data = loadData(args(0))
    partOne(data)
    partTwo(data)
  }

  def partOne(data: List[String]): Unit = println(s"part 1 result: ${data.map(_.toInt).sum}")

  def partTwo(data: List[String]): Unit = {
    var seen: ListBuffer[Int] = new ListBuffer[Int]
    var initial: Int = 0
    var found: Boolean = false
    seen += initial
    var innerLoopIterations:Int = 0
    while (found == false) {
       breakable {
         for (d <- data) {
           initial += d.toInt
           if (seen.contains(initial)) {
             result = initial
             found = true
             break
           }
           seen += initial
           innerLoopIterations += 1
         }
       }
    }
    println(s"part 2 result: ${result}")

  }

  def loadData(file: String): List[String] =
    Source.fromFile(file)
      .getLines.toList

}

