FROM rakudo-star
COPY . /perl
CMD cd /perl; set -eu; for t in t/*.t; do echo "==============\nTesting file $t"; perl6 $t; echo "\n"; done; echo "Tests successful"

