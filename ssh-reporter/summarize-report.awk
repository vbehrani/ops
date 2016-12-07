#!/usr/bin/awk -f

BEGIN {
  alphasense = "no";
  coresense = "no";
  wagman = "no";
  modem = "no";
}

END {
  printf "wagman %s\n", wagman
  printf "coresense %s\n", coresense
  printf "alphasense %s\n", alphasense
  printf "modem %s\n", modem
}

/2341:8037/ {
  wagman = "yes";
}

/2341:003e/ {
  coresense = "yes";
}

/1bc7:0021/ {
  modem = "yes";
}

/04d8:ffee/ {
  alphasense = "yes";
}
