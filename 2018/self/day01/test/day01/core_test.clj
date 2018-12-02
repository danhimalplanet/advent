(ns day01.core-test
  (:require [clojure.test :refer :all]
            [day01.core :refer :all]))

(def part1-data [{:in [1, -2, 3, 1], :out 3}
                 {:in [1, 1, 1], :out 3}
                 {:in [1, 1, -2], :out 0}
                 {:in [-1, -2, -3], :out -6}])

(deftest test-part1
  (testing "part 1"
    (doseq [test part1-data]
      (is (= (part1 (:in test)) (:out test))))))

(def part2-data [{:in [1, -2, 3, 1], :out 2}
                 {:in [1, -1], :out 0}
                 {:in [3, 3, 4, -2, -4], :out 10}
                 {:in [-6, 3, 8, 5, -6], :out 5}
                 {:in [7, 7, -2, -7, -4], :out 14}])

(deftest test-part2
  (testing "part 2"
    (doseq [test part2-data]
      (is (= (part2 (:in test)) (:out test))))))

;; eof
