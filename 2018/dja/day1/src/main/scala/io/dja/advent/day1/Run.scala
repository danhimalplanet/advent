package io.dja.advent.day1


import scala.collection.mutable.HashSet
import scala.io.Source
import scala.util.control.Breaks._

object Run {

  // credit to winkie for figuring out the speed woes
  var seen: HashSet[Int] = new HashSet[Int]
  var result: Int = _

  def main(args: Array[String]): Unit = {
    val data = loadData(args(0))
    partOne(data)
    partTwo(data)
  }

  def partOne(data: List[String]): Unit = println(s"part 1 result: ${data.map(_.toInt).sum}")

  def partTwo(data: List[String]): Unit = {
    var frequency: Int = 0
    var found: Boolean = false
    seen += frequency
    var loopIterations:Int = 0
    while (!found) {
       breakable {
         for (frequencyChange <- data) {
           frequency += frequencyChange.toInt
           if (seen.contains(frequency)) {
             result = frequency
             found = true
             break
           }
           seen += frequency
         }

         loopIterations += 1
       }
    }
    println(s"part 2 result: ${result}")

  }

  def loadData(file: String): List[String] =
    Source.fromFile(file)
      .getLines.toList

}

