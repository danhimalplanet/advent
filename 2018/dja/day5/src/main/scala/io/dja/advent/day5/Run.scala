package io.dja.advent.day5

import scala.collection.mutable.ArrayBuffer
import scala.io.Source
import scala.util.control.Breaks._

object Run extends App {

  var data = loadData(args(0))
  var stackFromData: ArrayBuffer[Char] = data.flatten.toArray.to[ArrayBuffer]

  var i = 0
  var changesDetected = false
  var finished = false
  breakable {
    while (!finished) {
      if (stackFromData.size == 0) break
      val next = i + 1
      val a = stackFromData(i)
      val b = stackFromData(next)
      if (a == b.toLower || b == a.toLower) {
        if (a.isLower && b.isUpper || b.isLower && a.isUpper) {
          stackFromData.remove(i)
          stackFromData.remove(i)
          changesDetected = true
          i -= 1
        }
      }
      if (next >= stackFromData.size - 1 && changesDetected == false) {
        break
      } else if (next >= stackFromData.size - 1 && changesDetected == true) {
        i = 0
        changesDetected = false
      } else {
        i += 1
      }
    }
  }

  println(s"Part 1: ${stackFromData.size}")


  def loadData(path: String): List[String] = {
    Source.fromFile(path)
      .getLines().toList
  }

}
