(ns day03.core-test
  (:require [clojure.test :refer :all]
            [day03.core :refer :all]))

(def part1-data {:in ["#1 @ 1,3: 4x4" "#2 @ 3,1: 4x4" "#3 @ 5,5: 2x2"]
                 :out 4})

(deftest test-part1
  (testing "part 1"
    (let [[overlap _] (part1 (:in part1-data))]
      (is (= overlap (:out part1-data))))))

(def part2-data {:in ["#1 @ 1,3: 4x4" "#2 @ 3,1: 4x4" "#3 @ 5,5: 2x2"]
                 :out "#3"})

(deftest test-part2
  (testing "part 2"
    (let [[_ fabric] (part1 (:in part2-data))]
      (is (= (part2 (:in part2-data) fabric) (:out part2-data))))))

;; eof
