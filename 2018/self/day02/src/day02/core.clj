(ns day02.core
  (:require [day02.helpers :as h]
            [clojure.string :as str]
            [clojure.java.io :as io])
  (:gen-class))

(defn part1
  [input]
  (loop [boxids input
         two 0
         three 0]
    (if (empty? boxids)
      (* two three)
      (let [freqs (vals (frequencies (first boxids)))]
        (recur (rest boxids)
               (+ two (if (h/has-frequency freqs 2) 1 0))
               (+ three (if (h/has-frequency freqs 3) 1 0)))))))


(defn part2
  [input]
  (let [num-boxids (.length input)]
    (first (for [i (range num-boxids)
                 j (range (+ i 1) num-boxids)
                 :let [diff (map #(= %1 %2) (nth input i) (nth input j))]
                 :when (= (count (filter not diff)) 1)]
             (str/join (map #(if %1 %2 "") diff (nth input i)))))))


(defn -main
  [& args]
  (let [input (->> (io/file "resources" "input.txt") slurp str/split-lines)]
    (println (part1 input))
    (println (part2 input))))

;; eof
