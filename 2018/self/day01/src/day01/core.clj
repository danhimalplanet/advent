(ns day01.core
  (:require [clojure.string :as str]
            [clojure.java.io :as io])
  (:gen-class))

(defn part1
  [input]
  (reduce + input))

(defn part2
  [input]
  (loop [freq 0
         repeated-input (cycle input)
         seen #{}]
    (if (contains? seen freq)
      freq
      (recur (+ freq (first repeated-input))
             (rest repeated-input)
             (conj seen freq)))))

(defn -main
  [& args]
  (let [input (->> (io/file "resources" "input.txt") slurp str/split-lines (map read-string))]
    (println (part1 input))
    (println (part2 input))))

;; eof
