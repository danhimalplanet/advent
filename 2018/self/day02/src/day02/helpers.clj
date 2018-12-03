(ns day02.helpers)

(defn has-frequency
  [freqs count]
  (some #(= % count) freqs))

;; eof
