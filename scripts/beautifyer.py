import mart
import mart_PRE
import mart_format
import importlib
importlib.reload(mart)
importlib.reload(mart_PRE)
importlib.reload(mart_format)

first = mart_PRE.rm_main()
second = mart_format.rm_main(first)
third = mart.rm_main(second)
