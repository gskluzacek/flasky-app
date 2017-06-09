#!/bin/sh

if [[ $# -ne 0 ]]; then
  diff -ENwburs app/ source_code/app/ -x'*.pyc'
  diff -ENwburs tests/ source_code/tests/ -x'*.pyc'
else
  diff -ENwburs app/ source_code/app/ -x'*.pyc' | grep ^diff
  diff -ENwburs tests/ source_code/tests/ -x'*.pyc' | grep ^diff
fi
