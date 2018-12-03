(ns day02.core-test
  (:require [clojure.test :refer :all]
            [day02.core :refer :all]))

(def part1-data {:in ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
                 :out 12})

(deftest test-part1
  (testing "part 1"
    (is (= (part1 (:in part1-data)) (:out part1-data)))))

(def part2-data {:in ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
                 :out "fgij"})

(deftest test-part2
  (testing "part 2"
    (is (= (part2 (:in part2-data)) (:out part2-data)))))

;; eof
