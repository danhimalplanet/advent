package io.dja.advent.day5

import scala.collection.mutable.ArrayBuffer
import scala.io.Source
import scala.util.control.Breaks._
object Run extends App {

  var data = loadData(args(0))
  var stackFromData: ArrayBuffer[Char] = data.flatten.toArray.to[ArrayBuffer]
  var keep: ArrayBuffer[Char] = new ArrayBuffer[Char]()

  var i = 0
  breakable {
    while (i < stackFromData.size) {
      val next = i+1
      if (next >= stackFromData.size) {
        break
      }
      val a = stackFromData(i)
      val b = stackFromData(next)
      if (a == '1') {
        stackFromData.remove(i)
        i = 0
      }
      if (a != '1' && b != '1') {
        if (a == b.toLower || b == a.toLower) {
          stackFromData(i) = '1'
          stackFromData(next) = '1'
          i = 0
        }
      }
      i += 1
    }
  }

  println(s"Part 1: ${stackFromData.size}")


  def loadData(path: String): List[String] = {
    Source.fromFile(path)
      .getLines().toList
  }

}
