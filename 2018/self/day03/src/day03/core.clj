(ns day03.core
  (:require [clojure.string :as str]
            [clojure.java.io :as io])
  (:gen-class))

(defn update-fabric
  [fabric top height left width]
  (loop [fabric fabric
         ltop top
         lleft left]
    (if (= ltop (+ top height))
      fabric
      (let [new-fabric (assoc-in fabric [ltop lleft] (+ 1 (nth (nth fabric ltop) lleft)))]
        (if (= lleft (+ left width))
          (recur new-fabric (+ 1 ltop) left)
          (recur new-fabric ltop (+ 1 lleft)))))))


(defn count-overlap-1
  [fabric]
  (loop [row 0
         overlap 0]
    (if (= row 1000)
      overlap
      (recur (+ 1 row)
             (+ overlap (count (filter #(> % 1) (nth fabric row))))))))


(defn part1
  [input]
  (loop [claims input
         fabric (vec (take 1000 (repeat (vec (take 1000 (repeat 0))))))]
    (if (empty? claims)
      (list (count-overlap-1 fabric) fabric)
      (let [[_ _ left-top width-height] (str/split (first claims) #" ")
            [left top] (map read-string (-> left-top (str/replace #":" "") (str/split #",")))
            [width height] (map read-string (-> width-height (str/split #"x")))]
        (recur (rest claims) (update-fabric fabric top height left (- width 1)))))))


(defn count-overlap-2
  [fabric & {:keys [start-row end-row start-col end-col]}]
  (loop [row (or start-row 0)
         overlap 0]
    (if (= row (or end-row 1000))
      overlap
      (recur (+ 1 row)
             (+ overlap (reduce + (subvec (nth fabric row)
                                          (or start-col 0)
                                          (or end-col 1000))))))))
(defn part2
  [input fabric]
  (loop [claims input]
    (let [[claim _ left-top width-height] (str/split (first claims) #" ")
          [left top] (map read-string (-> left-top (str/replace #":" "") (str/split #",")))
          [width height] (map read-string (-> width-height (str/split #"x")))
          totalsize (* width height)
          overlap (count-overlap-2 fabric
                                   :start-row top
                                   :end-row (+ top height)
                                   :start-col left
                                   :end-col (+ left width))]
      (if (= overlap totalsize)
        claim
        (recur (rest claims))))))


(defn -main
  [& args]
  (let [input (->> (io/file "resources" "input.txt") slurp str/split-lines)
        [overlap fabric] (part1 input)]
    (println overlap)
    (println (part2 input fabric))))

;; eof
