#!/usr/bin/python

import time
from enum import Enum

def final_input():
    return """77.FFFF|-77FFL-F-7--F7.|-7.F|7FFF|-FL7-777F.L-FL7.L7--7.|.7-.J-7-J.F-L77F-7-L7F-F.F7-FL-|--7--JF|7.-7FFL7F-F7-F.FF|-F7LF-FLJFLF-J.F7F--F77..
|-L7--|.FLJJL|FF7L|FF|-F.LJFLFLJ|L.LL-7L7J|L7.FJL||L7J|-|-777|.LF77|J|.F|L|..J|FL7L--7J.JL|7-|7F||F-FLJ|-F7|J||FF-7LLJ7J-JJ|-LJF.7-F|LF7|L7F
L7L|J-|F-77|F|J||.L|7JL|-7F-.|J.|-J77-7||J7LJ7|..L-L-7L7--|-F-J-L7J||F-|J.7-F.|77LF-JJ|FF|FLJLJLFJ7-|7FL---|LL|FJ-J7.|FF-7F|FJ-J-J.L|-|L7F7J
|7.J7FL-.||-F---J-LFJFF|.-LJ-J7FJF||||L|J.F..||F|L7JFF-7LF7||7|7||L-7LLL--J|LJ|LL.|7-LL-J-7..7JJF.7.7F7J-L.JJF|77..777LJ-7FF7F-JF7..|JF.F-L7
F-7--FJJ-FJ.-.FJ||.|7F.L|J.--LJ|-FJLL7-LJ-J-JJ7|-FJ.F--7F-7F7FF-|J.LFF7|7.|F.LL-J7J|7|LF|LJ.---FL7F7F77-JLJJ.FJL--|J.LJLFJ7J|JJ.JL--7JL-L--|
F-|-JJL|LLJ-|F-.J7LF7|-7F7LJ7JJFJ.-7|.|F|7JFL.F|F|FFJF-J|FJ||F7.J.F--J7|LFJFJ-F-J.7.F--F77.|.FFJJFJ||L-7.LLFF77JFLL|-J|F-JL7|LFJ-7FLJ7|.7.F|
L.L|.---7||.JJL||7F77L7FLJJF7.FL77.|JF-J|F7L-LJLFF7L7|JF|L7|LJ|.F7-|7.7J.7L7FF||FL7-|.L|||.--|J.FL7LJF-JF7F7|L7F7.|.-J|J.FL-J-FL7.|-JL7F|-L|
LF7FJJ||LLFJJ||L---L-7LJL|L7LJ77L77J7|L|JL-|7F-F-JL-J|F7|FJ|F-J-F7JL|FJL-JJL|7LL7|F-LF-JL7-.|JFFFJL-7L7FJLJ|L7LJ|7FF7.-.L-F|JJ|-7-|.FFF7F7FJ
.77JL-7.7|L|.F7|.L-J|JFJLJ-..L--FJL-JJ7J.-.L--JL----7||||L7||F--7F-7-|.LL77FLJ-|LFJFFL7F-JL||.FF|JF7|FJ|F--J7L7FJF-7F7LLJFL.FLJ-F7-|7|77F-|.
|-J|.-..|J7L7LL---|7|.|LF-JFF-FJJ|.-J---J.F-J|FLF7F7|||||FJ|||F-JL7|7777FFF|-L.FJ|-F.FJL---7-FF7JL|LJL7|L-7F7FJ|FJFJF7JJ.LJL-7|.7JFJ--JJ.|L7
J-FJ-J7FJLJ7|.JL|F-|-7|L7J|FJ.|-FL.JJ.L||F-|-F7-|||LJLJ||L7|||L7LFJL-7J7FJ-..|F77.F7FJF----J7|F77.L-7FJ|F-J||L7|L7L7|L7.|J||.LL.|7L||F-JFF7J
FF7JJFF7LLL|7-7|L7FLJL7-F7FF7F|F777J--F--FJFFJL-JLJF7F7LJFJ||L7L7|F--JJ7J.L-F7||LF||L7L7LF7|-FJL7.F-JL7|L-7||FJL7|FJ|FJ--7F-7.LFL||LFJJ.|JFF
FJL7F7FJ7FL-|LL7.L|--L-F77|||7L7F7F777|.FF7FL-7F7F7|||L-7L7|L7L7LJ|F7|JF-77J|||L-7||FJFJFJL77L-7L7L--7||F-J|LJF7|||FJL-777.|FF777.|FJJFLJJFJ
7-FJ-7|-|FF-|-||.L|7|.L||F7||7FFJ|||F--7-||FF7LJLJLJLJF-JFJL7L7L-7LJL7FJFJF7||L7FJ|LJFJF|F-JF7FJFJJF7|LJL-7L7FJLJ|||F7FJ-7-7LF77--J--FF7F7||
L-7.L||.L7J|LF7J||LFF7FJLJLJL-7L7LJ|L-7L-J|FJL-7F--7F7L-7L7L|FJF7|F--JL7L7|LJ|FJL7L-7L7FJ|F7||L7L7FJ|L7F--JFJL-7-|LJ|LJFJJ7|JLL--|7|F-JFLJ7J
|.|F7J7.F--J7LJJ.7LFJ|L-7F7F--J.L7FJF7L7F7|L7F-J|F-J||F-JFJFJ|FJLJL7F-7|FJ|F-JL7FJF-JFJL7LJ||L7L7|L7|L||F7-|F7FJFJF-J-F7.LL.F|L|.L7FL7FJLJ|.
|7JLL-77J.|.L--7-F7L7|F7LJ|L7F7FFJ|FJL7LJ||FJ|JFJL7FJ|L-7|FJFJL-7F-JL7||L7|L7F-JL7L-7|F-JF-JL7|FJL-JL-J||L7LJ|L7|FJF7F||F7J.FF7-F--7.FJ7J|--
L-JJ.FF7..L7|7J|FJL-J||L77L7||L7|FJL7FJF-J|L7L7L7FJL7L--J||FJF7FJL7F-J||FJ|FJL--7|F-J|L-7L7|F||L----7F-J|FJFFJFJ|L-JL7|LJL--7||7|F-J-|.|.||.
----F---|.LF-FF7L---7||FJF7|||FJ|L7FJL7L-7|L|FJFJL-7|F7F7LJL7||L7FJ|F-J||FJL7F--J|L-7L-7L7|F7||-F---JL-7||F7L7|-|F---JL7F---J|L7|L-7JJ|.7L|J
L|LLJ.|JL|-|-FJL----JLJ|FJLJLJL7L7|L7FJF-J|FJL7|F--JLJLJL7F-J|L7|L7||LFJLJF7|L--7L7-L7FJ7|LJLJL7L---7F-J|LJ|FJL7|L---7FJL-7F7|FJ|F-J.7LF7-LJ
.L7.|7|FF-777|F---7F7F7||F-----JFJL7|L7L-7|L-7|||FF--7F7J|L-7L7||FJ|L7L-7FJLJF7FJFJF7|L--JF----JF7F7|L7FJF-JL-7||F---JL7F-J||||FJL---7-.JFJ|
|JJLJ.FFL7L77||LFFJ|LJ|LJL7F---7L7FJ|FJF-JL--JLJL7L7FJ|L7|F-JL||||.|FJF-JL--7|||FJFJ|L---7|F7F--J||||FJL7|F--7||||F7FF7||-FJ||LJF7F--JL-.7JL
L7.|L|JF-JFJFLJF7L-JF-JF-7||F--JFJL7|L7L----7F7F-JFJL7|FJ|L7F7|||L7|L7L7F---J|LJL-JFJF---J|||L--7|||||F7|||F-J|LJLJL7|||L7|FJ|F-JLJ7LLJ...L|
.L7F-7FL-7L7F-7|L---JF7|FJLJL--7|F-JL7|F7LF7||LJF7L-7LJL7L7LJ|||L7|L7|FJL---7L--7F-J7L--7FJ||F7FJLJ|||||||||F7L--7F-J|||FJ|L-JL--7||.F7-77FL
L-|--F7F7L7LJFJL7F7F7|LJL-7F---J|L7FFJ||L-JLJL77|L77L-7FJFJF7||L7||FJLJF-7F-JF--J|-F7F7FJL7|LJ|L-7FJ|||||||||L-7F|L7FJLJL-JF---7FJJ.F7||JF-J
|J.|.||||FJF-J7-LJLJLJFF7FJL7FF7|FJFJFJL--7F-7L7L7L7LFJL7L-J||L7||LJF--J.LJF7L7F-JFJ||||F-J|F7L--JL-J||LJ||LJF-JFJFJL7F-7F7L--7|L7.77|F-7-J.
F-F-FJ||||FJ|F777F-7F--J|L-7L7|||L7L7L7F7-LJ|L7L7|FJFJF-JF7FJL7|LJF7L7F77F-J|FJL-7L7|||||F7||L----7F-JL7FJ|F-JF7L7L77||7|||F--JL-JF|--FJ|7.|
|F|7L7LJLJL7FJL7FJFJL--7L7|L7|||L7L7|FJ||F-7F7|FJ||-L7|F7||L-7LJF-JL-J|L7L-7|L--7|FJLJLJLJ||||F---JL--7||FJL--J|FJFJFJL7LJ|L--7F7F7L|-|.F|F-
LL77FL---7FJ|F-J|FJ|FF7|FJF7||||-L7||L7|LJFJ|||L7|L7FJ|||||.FJF7L--7F7L7L7FJ|F7FJ|L-7F-7F-JLJFJF-----7LJLJF----JL7L-JF7|F7L--7|||||JF-7FL-7J
7-F77LF7FJ|FJL--JL-7FJ||L-J||||L7FJ|L7|L-7L7|LJFJ|FJL7LJLJL7|FJL---J|L7|FJL7LJ||FJF7|||LJ|F7FJFJF7|F7L7F-7L7F7LF7|F7FJ|LJL--7LJ|||L7J-J77||7
-J||F-JLJFJL----7F7|L7|L--7||||FJL7|FJL7FJFJL-7|FJ|F7L----7LJL--7F7FJFJ||F7L-7LJ|L|LJ|F7F7||L-JFJ|FJL7|L7L-J|L7|||||L7|F7F-7L--JLJFJ-|LFL7L7
|7||L---7|F7LF--J||L-J|F7FJLJLJL7-||L-7|L7L7F-JLJFJ||F7F--JF7F--J||L7|FJ||L-7L7FJFJF-J|||||L-7FJFJ|F7LJFJF77L7LJ||||FJ||||7L7F---7L7.-7|||-L
F-JL----JLJL7L---JL-7FJ|||F7F-7FJFJL-7||-|FJL-7F-JFJ|||L-7FJLJF7J|L7|||FJ|F-JL|||L7|F7|LJ||F-JL7|LLJ|F7L-J|F-JF7LJ||L7LJLJF7|L7F7L7|.||-FJJ|
L--7F7F7F7F7L7LF7F7FJL-JLJ|||FJL7L-7FJ|L7||F-7|L-7L7||L7FJL7F7|L7|FJ||||FJL7F7|L7FJ|||L7FJ|L7F7|L7F7LJ|F--J|F-JL7FJL-JF---J|L-J|L7LJFFLJLJ-|
FLFJ|LJ||LJL7L-J||LJF-7F7FJ|||F7L--J|7|FJ||L7|L-7|J|||FJ|F-J||L7|||F||||L7FJ||L7||FJ||L||J|FJ|||FJ||F7||F7F||F77LJF7F-JF7F7L7F7|FJF7--7J|F7J
|FL-JF-JL7F7|F-7LJF7|7LJLJ7LJLJL---7L7|L7|L7||F7|L7||||FJL7FJL7||||FJ|||FJL7||FJ||L7|L7||FJL7||||FJ||||||L-JLJL-7||LJF-JLJL7LJ||L-J|LL|F77J.
L7|.LL7F7||LJ|FJF7|||F--77F7F-----7L7LJFJ|JLJLJ|L7||LJ|L7FJ|F-J|||LJ|||LJF-J||L7||FJ|LLJ|L-7||||||FJ|LJ||F--7F-7L7L-7L----7|F7||F--J.LLF-7-7
LL-7.LLJLJL-7|L-JLJLJL-7L7||L7F7F7L-JF7L7L-7F--JFJ|L-7|FJ|FJ|F7||L--7||F-JF7||FJ||L7L--7L7FJ||||LJL7L-7|||F7LJ-L-JF7|F----JLJLJ||F--7F77.|.|
FJF7--7F7F--JL-7F7F---7L7|||.LJLJL---JL7L7FJL--7|7|F7||L7||FJ|LJL7F-JLJ|F7|||||-|L7|F7FJFJL7|||L7F-JF7|LJLJL--7LF7|LJL--7F7F---J||F-J7F7F-7L
L|-J-7FJLJF7F--J||L7F7L-JLJL-7F7F------J-LJF7F-JL7||LJ|FJ||L-JFF-J|7F7|LJ|||||L7L7|||||7L7FJLJ|FJL-7|LJ|F-----JFJLJF7F--J||L7F--J||F|FJ|JJ7.
F|..FFL7F7|||F--J|FJ||F7F--7FJ||L---77F7.F7||L-7FJLJF7||FJL7F--JF7L-JL-7FJ||||FJ7LJ|||L-7||F-7|L--7||FF7L7F----JF--JLJF7J||-|L77FJL-7L7|F|JL
FLFFFFJLJLJLJL--7|L-JLJ||F-J|FJ|-F--JFJL-J||L--JL---J||||F7|L7F7|L7F---JL7|||||7F7FJ|L7FJLJL7LJF7FJ||FJL7LJF---7L--7F-J|FJL7|FJFJF-7|FJL-77J
-7L7.LFLF---7F--J|F--7|LJL-7|L7L7L---JF7F-JL-7F7F-7F-J|||||L7LJ||FJ|F7F--J|LJ|L7|LJFJ|LJF7F7L-7|LJ|LJ|F7L--JF-7|F-7|L7FJ|F-J|L7|FJFJ||F--JJ.
LFLJ7LJ-L--7|L--7|L-7|F--7FJL-JFJF7F7FJ|L---7|||L7|L7FJ|LJ|FJF-J|L7LJ|L-7FJ-FJFJ|F7L7F--JLJL--JL-7F-7LJL----JFJLJ7LJFJL-JL-7|FJ||7L-J||F7FF7
L|F--F-LF7FJL---JL-7||L-7LJF7F7L-JLJLJ-L7F7FJLJL7||FJL-JF-J|7L-7|FJF-JLFJ|F-JFJFJ||FJL7F---7F-7F7||FJF----7F7L7F7F77L7F----J||FJL7|F-JLJL-J|
F-J-FJ.FJLJF-7F7F-7LJL77L--JLJL7F7F7F--7||||F---J||L---7|F7L-7FJ|L7L--7L7|L-7|JL7|||.FJ|F--J||||LJ||JL7F-7LJL7LJLJL--JL-7F7L|||F7L7|F-7F---J
F|-FLJ-L---JLLJLJJL-7FJF7F----7||LJLJF7||||||F--7||F7F-JLJ|F7||FJFJF7FJ-LJ7FJL-7LJ|L7L7|L7F7|FJ|F-J|F-JL7L-7J|F--7F-7F-7LJL-JLJ|L7LJL7|L--7J
F-7|-F---7F7-F-7F7F7||FJLJF7F7|LJF--7|LJLJ|||L7FJ|||LJF--7|||||L7L7||L-7-F-JF-7L-7L7L7LJLLJ||L7|L-7|L---JF7L7|L-7LJFLJFJF7F-7F-J|L-7FJ|F-7L7
--FJ7L--7LJL7L7LJ||LJ|L---JLJ|L-7L-7LJF-7.LJL7|L7||L-7L7FJLJ||L-JFJ|L7FJFJF7L7|F-J-|FJF---7LJ-LJF-JL-----JL-JL-7L----7L-J|L7|L---7-LJJ|L7|FJ
|FJ||J||L7F7L7|F7LJF7L--7F7JFJF7|F7L--JFJF7F7|L7||L-7L-JL7LFJL--7L7|LLJ7L7||FJ|L--7LJFJF-7L-7|F7L7F-7F-7F-7F--7L7F7F7L--7L7|L7F-7L---7|FJLJ7
F|.7J|FF-J|L7LJ|L7FJ|F-7LJL7L-J|LJL----JFJLJ||FJ|L7-|F7F7L7L7F7FJJLJF7.F-J|||FJF7FJFFJFJFJF7L-JL-JL7||FJ|FJ|F-JFJ|||L-7FJ|LJF||7L----JLJJ|7|
F|FJ--FL7FJF|F7|FJL7LJF|F-7|7F-JF------7|F--JLJJL7L7|||||FJFJ|||F---JL-JF7|LJ|FJ|L-7L-J|L-JL7F---7FJ||L-JL-JL-7L7||L-7|L---7FJL-------7LFLJ|
FLL7|LJLLJ7FLJ||L--JF--JL7|L-JF7|F--7F7LJL-7F7F-7|FJ||||LJLL7||||F--7F-7|||F-JL7|F-JF-------J|F--JL7||F-------J7LJ|F7|L--7FJL7F-7F--7FJ.|.||
7L|-|JLLLF-7F7LJ-F7-L7F-7|L7F-J||L-7LJL---7LJLJFJ|L7|||L--7FJ|LJLJF-J|.||||L7F7||L-7L------7FJL-7F7|LJL--7F7F7F--7LJ|L--7|L7||L7|L-7LJ7-L.L|
L7||LF.LFL7LJL7F-J|F-J|J||FJ|F-JL7FJF----7|F7F7|F|FJ||L7F-JL7L---7|F7L7LJ|L7||LJ|F-JF-7-F--J|F--J|LJ|F7F7LJLJLJF7L7FJF--J|FJFJFJ|F-J.||F|7|F
|-|-LJFF7.L--7|L-7LJF7|FJ|L7|L7F7|L7|F---JLJLJ|L7||LLJLLJJF-JF7F-J|||FJF-JFJ||F-JL-7|FJFJF--JL-7FJF-7|||L------JL-JL-JF-7|L7L7L7|L----77L7JJ
-7|.FLF|L-7F7||F7L-7|||L7L7LJ.LJ|||LJL--7F7F77L7||L-7L|F--JF-J||F-J||L7|F7L7LJL7F-7||||L-JF--77LJ.L7||LJF7F7F------7-FJFJL-JJL7||F----J7-.|.
FJ7FFJFL-7||LJLJL--J|||7L-JF----J|F-----J|LJL-7LJL--J7FJF-7L7LLJL-7|L7|LJ|FJF7.||FJ||L--7FJF7L-7F7FJ||F-JLJLJF----7L-JFJF7F7J|LJ|L--7LLJFF-7
|LFJ.7LLFJLJF-------JLJF-7FJF7F7FJL------JF7F-JFF7F7F7L-JFJFJ.LF7FJL7||F-J|FJL-J|L-JL--7|L-JL-7|||L7|LJF--7F-JJF-7L7F7L-JLJL7F-7|F--JJ.LL|.F
|7||-777L--7|F--------7|FJL7|||LJF------7FJ|L--7|||||L-77L-JF|L|LJF7|LJL7FJ|F7F7|F7F-7FJ|7F7F7|LJL-JL--JF7LJ-F7L7|LLJL7F----J|FJLJF-7.F.|J7J
7JLLF.FF7F-J|L----7F-7LJL-7LJLJF-JF7F7F7LJLL---J|LJLJF-JF----7-L-7|LJJ-|||FLJ|||||||FJL7L-JLJLJF-7F7F--7||F--JL7||F7F7LJF7F7FJL---JFJ-|-J-F7
.L7J|F-JLJF7L7F7F-J|FJF7F7|F-7JL--JLJLJL7FF-7F7FJF7F-JF7|F---JF--J|F7J7FLJF--J|LJ|LJ|F7|F-7F---J7LJLJF7LJLJF7F7LJLJLJL--JLJLJF-7F--JJFJ.|7||
7-|7F|F7F7||FJ||L--JL7|LJ||L7L--7F7F-7F7L7L7||||FJLJF-JLJL--7LL--7LJL77LJJL7F7|.FJF7LJ|||FJ|F--------JL-7F-J|||F7F7F-7F-7F7F7L7||F7JF|.J7|-J
L7LJ-LJ||LJLJFJL7F--7LJF-J|FL--7LJLJJLJL7L-JLJLJL-7||F-----7|-LLFJF-7L-7L7FLJLJ7L-JL-7|||L-JL--7F---7F-7LJF7LJLJLJLJ|LJFLJLJL-J|||L-7.L7LJ||
|FF||.LLJ-F77L-7|L-7|F7L-7L---7|F--7F--7|F-------7L-JL---7FJ|7|LL-JJL--J77-F7F7F7LF--J|LJF----7||F7-LJJL--JL--7F7JF77F-----7F77LJ|F-J7.FJF7-
F-|L-7FJ.FJ|F--JL-7||||F7L---7|LJF7LJF7|LJF-----7|F----7FJL-J7LJ.L|7-LLL-F-JLJLJL7L--7L7-L---7|LJ||F----------J|L-JL7|F----J|L7JFJL--77F7||J
J-L7LJJJ7L7LJF-7F7LJLJLJL----JL--JL--JLJF7|F--7FJLJF7F7LJJLLF7FF---J.|JLFL--7F--7|LF7L7L7F7F7||F-J|L--7F----7F7|F--7LJL-7F7-L7|FJF---J-JJ7||
J7-J7J|7FFJF-J-LJL-7F---7F7F-------7F--7|LJL-7|L7F7|LJL7F7JL||7J.|JFJJ..LF--J|F-JL7||FL7LJLJ|||L7FJ-F7||F-7FJ|||L7JL7F-7LJL7FJLJFJF7F7J|---J
F|JJ|FJ-FJFJLF77F7FJ|JF-J|LJF7F7F--J|F-JL-7F-JL-J|||F-7L7F7FJL77.7F|J|..|L7F-J|F-7LJ|F7|F--7LJL-J|F7|LJ|L7|L-JLJFJF7LJJL---JL7F7L-JLJL-7-7|J
7||F|7--L7|F-JL-JLJFJFJF-JF7||||L---JL7-F7|L--7F7|||L7L-J|LJF7L77.-JF7J--LLJ|FJ|FJF7LJ|LJF-JF-7F7|||L--J-|L7F7F7L7|L-7F7F7F7FJ|L7F-7F7FJJ|LL
|FLFJF-JLLJL---7F7FJ-L-JF-J||LJL-----7L7|||F--J|||||FJ7F7L7FJL-J77|.|L|.|FF7-L-JL-JL-7|F7|F7|F|||LJL7F-7FJLLJLJL-J|F-J|||LJLJFJ-LJ7LJLJ|.-..
FJ.|L|J|7F-----J|LJ|F7F7L-7|L--7F---7L7LJLJL---JLJLJL7FJL-JL---7-7L-J7JFFFJL-----7F7FJLJLJ|||FJ||F-7||FJL7F7F--7F7||F7||L7F-7|F7LF-7FJ--|FL|
-J-L-|FF-L-7F7F7|F--JLJL--JL---J|F--JLL7F7F-7F7F7F7F-J|F-------J-J.JL|7FLL------7LJLJF7F7FJ||L7|LJFJLJL--J|LJF7LJLJLJLJL-JL7|LJL-JFJ7J-L--7|
F|-F-|-J|F-J|||LJL-7F7F-7F7F7F7FJL----7|||L7||||LJLJF-JL--7F7F7F7.7J7|F7|-LF7F-7L7F-7|LJ||FJL7LJJFJF-7F7F-JF-JL---------7F7|L7F--7L7.|.FL-7J
F|.F-F7F-L7FJ||F---J|LJFJ|LJ||LJJF----JLJL-JLJLJJF7FJF----J|LJLJL-7-FF7F7FF||L7L-J|FJ|F7LJL-7|F--JFJ-LJLJF7L-----------7||LJ||L-7L-J-JF7L777
7L-|7.FJFLLJ.LJL----JF7L7|F-J|JF7L--7F7F--7F7F7F7|LJFJJF77FJF7F---J.FJLJ|F-JL7L---J|FJ|L--7JLJL--7|F-----J|F-----7F7F7FJ|L--7|F7L--7-LLJF-JL
|.|.FFJJ7FJ--J|.F7F7L||.LJL-7|FJL---J|LJF-J|||||LJF-JF7||FJFJ||F7F-7L7F-JL--7L7F7F-JL7L--7|F7F7F-J|L-----7|L--7F7LJLJ|L7|F7FJ||L7F7L77J-LJ..
LF..JJ.F-|F7--F-JLJ|FJL-----J|L----7FJF-JF7|||||F7L--JLJLJFJ.LJ|LJFJFJ|F7F-7L7LJLJF7FJF--JLJLJ|L--J.F7FF7|L--7LJL---7L-J||LJJ|L7||L7L7-77|FJ
7L-7JJ7F||FFJFL---7|L7F-7F---J|F7F7LJFJF-JLJ|||||L-7F7F7F-JF7-FJF-JFL7|||L7|7|F7F-JLJ|L-7F---7|F7F--JL-JLJF-7L7F-7F7L--7|L--7L7||L7L-J|F7F|J
LF.|.|7.|7||-F-7F-JL7LJJLJF----J||L--JLL7F--J||||F7LJ||||F-JL7|FJF7F7||||FJL7LJ|L7F--7F7LJF--JLJ|L--7F----JFJ|LJ7LJL---JL-7FJFLJL7L7J-JFLJJ|
F|-|7LL-L--JFL7|L--7|F7LF7L----7LJF-7F7FJL---JLJLJL-7LJLJ|F--J|L7|LJLJLJ|L-7L7JL-JL-7||L-7L----7|JF7|L7F---JF-----------77LJF7F7-L7|JFJFJL7|
|7.7J7|FJJ.FF-JL---JLJL-JL----7|F-JFJ|LJF7F7F7F7F7F-JF7F7||JF7|FJL-7F--7L-7L7|F7F7F-J|L7FJF---7|L-JLJFJ|F--7L7F--7F-7F-7L7F7|||L-7||FFFJ7.|7
LFJL|FF7--F7L------7F------7F7LJ|F7L-JF7|||||LJ||LJF7|||LJL7|LJL-7J|L-7L--J||LJ|||L-7L7|L7L7F7LJF-7F-JFLJF-JFJL7-|L7||JL7LJLJLJF-JLJJJJL|-L|
|.|.L-JJ7||L7F----7||F-7F77LJL--J|L--7|LJ||||F-JL--JLJLJF--JL7F7FJFJF7L7F7F7L-7|||77L7||FJL||L-7L7LJF-7F-J|FJF7L7L-J|L-7|F7F7F7|JLJ7|FJ..|7.
FLLFJ7L-|-|FJL---7LJ|L7LJL--7F---JF-7||F7LJLJL7F7F-7F--7L-7F7||LJFJFJL7||LJL7FJLJL7F-JLJL-7LJF7L-JF7L7|L---JFJL7L77FJF-JLJLJLJLJ-FJ-|..|.|L-
|7LJF|J.LFJ|F7F-7L-7L7L-7F-7LJF---JFJLJ|L----7||||.|L7FL--J|||L-7|FJ-LLJL-7FJL---7|L-----7L7FJL---JL-J|7F---JF7L7L7L-JF-------7|||FF7F-F-|J7
|FJ-|JJ-LL7LJLJFJF7L-JF7LJ-L7FJ-F--JF7FJF----JLJ|L7|FJF--7FJ|L7FJ||F7F7F7FJ|F7F-7|L---7F-JFJ|F----7F-7L7L--7-|L7L-JF77|F------JJ.|L|L|JLL|-J
7|L-L--.-FL---7L-J|F7FJL-7F7LJF7L---JLJFJF-----7L7|LJFJF-JL7|FJL-JLJLJ|||L7|||L7|L-7F-JL-7|LLJF---J|JL7L7F7L-JFJF7FJL7|L---7LF77FLF7F|.F7LFJ
FJ-FJ-J7.F7F-7L--7|||L7F7LJL--JL------7L7|F----JJ|L-7L7L77FJLJF-------J||FJ|||.||-FJL7F7FJL-7|L7F7FJF7L7LJL---JFJLJF7||F---JFJL7F-J|--FJFFJJ
|.FJ--.F-JLJFJF7FJLJL7LJL7F7F7F7F7F--7L-J|L--7F7FJF7L7L7L7L--7|F-7-F-7.||L7LJL-JL7L-7|||L7F-JF-J|LJFJL-JF-----7|F--JLJ||F7F7L7FJ|F-J.|F-|J7|
L-L7.|-L-7F7L-J|L---7|F7F||||LJLJLJF7L---JF--J||L-J|FJ|L7|FF-J||FJFJFJFJ|-|F7F7F-JF-JLJ|FJL7|L7FJF-JF---JF7F--J||F7F77|||LJL-JL7|L7J--.|LJ-F
|.|L77-|JLJL--7|F7F7|LJL-J|LJF-----JL--7F7L---J|F-7LJF7FJL7L-7LJL7|FJFJFJFJ|LJLJF7L--7FJL7FJF7LJFJF7|F-7FJ|L---JLJLJL-J||F-7F-7LJFJ|-L7JJ|L|
.F7.||-F7-F---JLJLJLJF-7F7|F-JF-----7F7LJ|FS---JL7|-FJLJF7L7FJF--J||-L7L-JFJF-7FJL--7||F7|L7||F7L-JLJL7|L7L---------7F7LJL7|L7|F7L7FF-FJF77|
-7L-|7FJ|7L-----7F7F7L7||LJ|F7|F7F--J|L-7||F-7F-7|L7L7F-JL7|L7L7F7|L-7L--7||L7|L-7F7||LJLJFJ|||L7F7F--J|FJFF-7F----7|||F--JL-JLJ|FJ7-.77|L|.
|L..LFL7|F------J|||L7|LJF7LJ|||LJF--JF7|||L7|L7||FJ-LJF7FJL7|FJ|||F-JF7FJL-7|L-7LJ||L---7L7||L7LJ|L--7|L-7L7LJF---JLJLJ7F-----7LJFL77|FF-77
FJF-J.FJLJF-7F7F7|||FJ|F-J|F-J|L--JF7FJLJ||.|L7|LJL7F7FJ|L-7LJL7|LJL-7|||F--JL7FJF-JL-7F-JFJ|L-JF-JF--JL--J-|F7L--7F7F7F7|F-7F-JF77.J|7|JFLJ
|.||-FJF-7|FJ|||LJ|||FJ|F7LJF-JF7F-J||F77LJFJFJ|F--J|LJFJF7L7F-JL7F--J|LJL---7|L7L---7|L-7L7L7F-JF7L-------7||L---J|||LJLJL7||F-JL7JJ|LJFJ7J
7-F-JL7|FJ|L7|||F-J|||7LJL--JF-J||F7LJ|L7F7L7|L|L--7L7FJFJL-JL--7|L7FFJF-----JL7|F7JFJL7FJFJ.|L7FJ|F---7F-7LJL-----JLJF---7|LJ|F--J77L|LJL77
|F7F-LLJL-J-||LJL-7|||F---7F7L-7|LJL--JFJ|L-JL7|F--JFJL7L---7F-7|L7|FJFJF---7F7|||L7|F7||FJF-JFJ|FJL--7|L7L--7F-------JF-7|L7J|L---77.L-|-|F
J-L7JLJ-F---JL7F--J|LJL--7LJ|F7|L-----7|LL7F-7|||F7FJF-JF7F7||FJ|FJLJFJFL7F-J|||||FJLJ|LJL7L-7L7|L7F-7|L7L--7|L----7F--JFJL7L-JF--7L7JJJJFJ|
JLJJ-|F-JF7F-7|L---JF7F--JF7LJ|L-----7||F7LJL|||LJ|L7||FJ|||LJL7||F--JFF-J|F7||||||F7J|F-7L--JFJL7|L7|L7L--7||F7F-7LJF7FJ7.L7F-JF7L7|F-JFJ-|
J.|LFL|F-JLJ|LJF----J|L---JL-7L------JLJ||F7FJ||F-J7|L7L7LJL--7|LJL-7F7|F7||LJ||||LJL7||FJF--7L-7|L7||FJF77LJLJLJ7L--JLJF7F7|L--JL7LJJ--|-F-
LFL-L.LJJLF---7L----7L---7F7JL-7F---7-F7||||L7LJ|-F7|FJ7L-7F7FJL7F--J||LJ||L7FJ||L--7|LJL7|F7L--JL7|||L-J|F7F----------7|LJ||F7F7FJLFJ7LF-7.
.|.|--|L|JL7F7L----7L---7LJ|F77LJ7F-JFJ||LJL7L-7|FJ||L7F-7||LJF7|L7F7|L7FJ|FJL-J|F7FJL7F-J||L7F7F7||||F7FJ|LJF-----7F-7LJF-JLJLJLJFF7JL-L.|-
|JF-JFJ7|7F|||F7F-7|F7F7L-7LJ|F7F7L7JL7|L7F-JF7|||FJ|FJL7|||F7|||FJ|||FJL7|L7F--J||L-7|L-7||FJ||||||||||L-JF7L--7F7LJJ|F7L7F----7F7||7|.F|J|
.|LJ.J77LJFLJ||LJFJLJ|||F7L-7LJLJL-JF7|L7|L-7|LJLJ|FJ|F7|||LJ||||L7|||L7FJ|FJL7F7||F7|L7FJ|||FJ|||||||||F7FJ|F-7LJL7F7LJL-J|F---J|||L77F7.L7
7FF-FJF|J||F7LJF7L--7LJLJL-7L-7F--7FJ||FJ|-FJL-7F-J|7||LJLJF-J||L7LJ||-||FJ|-FJ|||||||L||FJ|LJJ||||LJ||LJ|L7|L7L7F7LJL7F7F7||F-7||||FJ.-.-FF
|FLF|-|||FFJL7FJL-77|F--7F7L7.LJF-J|FJ|L7L7L7F7||F7|FJL---7L-7|L7L7FJL7LJL7L7L7|||LJ||FJ|L7L--7||||JFJL7FJFJL7|FJ||F-7LJLJLJLJFJFJLJ|7-J77|J
7.FJJLLL-FJF7LJF-7|FJ|F-J|L7|F--JF7||FJFJFJFJ|LJ||||L7F7F-JF7|||L7||F7|F--JFJJ||||F-J|L7L7L-7FJ||||FJF7|L7|F7LJL-J|L7|F7F-7F-7L7|F7FJ7-|||7J
7-|||LL7JL7||F7|FJLJFJ|F7|FJLJF7FJ|||L7L7|FJFJF7LJLJFJ||L--J|||F-J|||LJ|F7FJF-J|||L7FJFJFJF-JL7||LJL7||L7|LJL7-F-7|FJLJ||||L7|FJ||LJF7F7-.L7
|||F-7F|7LLJLJ||L7F7|LLJ||L7F7|||J|||FJFJ|L7L-JL7F77L7||F7F7||||F7||L-7|||L7L7FJ|L7|L7L7|7L7F-J||F--J||FJ|F-7L-JFJLJF7FJL7|FJ||.||F-JLJ|77-7
|77.|7|L7FJ-|LLJFJ||L7F-J|FLJ|||L7LJ||FJFJFJF---J|L7J||||||LJ||LJ||L7FJ|||FJFJ|FJFJ|FJFJL7FJL-7LJL--7|||FJL7L7F-JF--J||F7||L7|L-JLJF7F-JJJ7|
7J7--LJLL-..LF--JFJ|FJ|F-JF--J|L7L-7|||FJJL7L----JFJFJ||||L-7|L-7||FJ|-LJ||.L-J|FJLLJ.L7FJL7F7|F----J|||L7FJ||L--JF--J|||||FJ|F7F7FJLJ7JL..|
LL|JLL7-J|.7.L--7L7LJFJ|F-JF7FJFJF-J||LJF7FL7F--7FJFJFJ||L-7|L7FJ||L7L-7FJL-7F-J|F-----JL7F|||||F-7F7||L7|L-7L---7L--7LJLJLJ||||||L-7F|7|F|J
|-J7LLJ|F--JFFLJL7L7FL7|L-7|LJFJFJF-J|F-JL--JL-7|L7L7|FJL-7LJFJ|FJL7L7FJ|F7FJL7FJL7F7F7F7L7LJLJ||FJ||||FJ|F7L-7F7L---JF7F----J||||F-J77-|-J7
.7F7.L---7..F---JL7L-7||F-J|F-JFJFJF7|L7F7F7F7FJL-JFJ|L7F7L7JL-JL7FJFJL7||||F-J|7FJ|LJ||L7L7F7.LJL7|||LJFJ||F7LJL---7F||L--7F-J||LJ|.LJ-|.FF
.LFLJ.||.L.FL|-7-||F7|LJL--JL-7L7|FJLJL||LJLJ||FF7.L7|FJ|L7L---7FJ|FJF7|LJ|||F7L7|FJF-JL7L7LJL7|F-J||L77L7|LJ|F7F7F7L7||LF7LJLL||J-|77FFJ77-
..||.FLJJFF7---LFFJ|||F7JF----JFJLJF7F7|L7F7FJL-JL7L||L7L7|F---JL-JL7|||F7||||L-JLJ-L---JFJF-7L7|F7|L-JF-JL7FJ|LJ|||FJ|L-JL77.LLJJ||F|-|L|J|
7J--JJ7|L7LJ7L7LFL7||||L-JF7F-7|F--JLJLJFJ||L7F7F7L7LJ||FJ|L-7F-7FF-J|||||LJ|L--7F7F----7L7|FL-J||||F--JF7FJL7L-7LJ|L-JF--7L-7-JL-7JL7J|.--L
L7-|LJ|J-77F7L|-F-J|LJ|F7FJ|||LJL7F-7F-7L-JL7LJ||L7|JF-J|JL-7LJFJFJF7||||L7FJF7FJ||L---7|FJL--7FJ|||L-7FJ|L-7|F7L-7L7F-JLFJF7|J-7F7-7|.-7.|.
J7.---J|L|L-J.L-L--J-FJ|LJ|LJF---J|L||-|F7F7L7FJL7LJFJF7L--7L--JFJFJ|||LJFJL7|||FJL----JLJF7F-J|FJLJF-JL7L7FJ||L-7|.|L--7L-JLJ.LFLJ-|--L7-7-
L|F|-7L7-J||.F7FJ7|7-L7|F----JF7F7|FJ|FJ||||FJL7FJF-JFJ|F7FJLF-7L7|-LJ|F7L-7||||L7F--7F7F7||L7FJL--7|F-7|FJ|.|L-7LJFJF7FJJFL|JFF-7L7L|L|L-J|
F7---L7J7F|FJ-|-LJJJ-LLJ|F7F-7|||||L7|L7|||||F-JL7|F7|FJ|||F7|FJJ||F--J||F-J||||-LJF-J||||||FJL-7F7|||FJ|L-JFJF7L7FJFJLJJFJ-|LFF-7|L-F-FJ.FL
LJLL-LL.|-FJJ|J|.|.LF7FL|||L7LJ||||FJ|-||LJ|||F7FJLJLJL7||LJLJL-7LJL7F7||L77|||L7F7L7FJ|||||L--7||||LJL7|FF7L7|L-JL7L--777FFL7LJFFL7.F.7J7F.
.|.|.LJ--.|J.L77J77|FL||LJL-JF-J|||L7L7|L-7||LJ|L7F----J||F7F7F-J-F-J|||L7L7LJL7||L-JL7LJLJL7F-J||||.F-J|FJL-JL---7|F--JLL-FJ|.LLJJL-JFL-J-7
L-J7--J7|.F.F--7FFLJ.LL77||..L7FJLJFJFJ|F7|||F-JFJL----7|||||LJF-7L-7||L7L7L-7FJ|L7F7FJFF---JL-7|||L7L-7|L-7F7F---JLJF7-FF7|F|-LLJ.||FF7LJ|.
F|.L7||-J7J-J-L77.|L-F7|-J7.F-J|-F-JFJJLJLJ|||F7L-7F---J|LJ|L7||FJF-J|L-JJL7FJL7|JLJ|L-7L7F-7F7|LJL7|LFJL7FJ||L------J|FLLJL-77J.FFJ-7LF7LF-
LF|J|FJ-LF--J.|L|.|-FLJJ7F|-L7FJFJF7L-7JLJLLJ||L--JL---7L-7L7L-JL7L-7|F----JL-7||F--JF-JFJ|FJ||L-7FJ|FJF7|L7|L7F7F7F-7L77|-||.|.FFFJL7-L-.L7
.FJ-|7|-LL.FJFFF--J.|-.FJ-JL|||.L7||F-JLLJJ-FJL7.F-----JF7|FJF7F7|F-J|L-7F7F7FJ||L--7|F7L-J|FJL7FJL-JL7|LJFJ|FJ||||L7L7L7L7-J----.L77|7|-F.J
-|J.L7---J7|FL-J-7-|JLF-J7LFFJL7FJ||L7J.F|.FL7FJ-L-7F7F7||||FJ||||L-7L7|||LJ|L7LJF--JLJL--7LJ.LLJ|J.J.LJL|L-J|FJ||L7L7L7|--J-JF||77L-JL77J||
FL|-L--7-J7|J7|LF|.-..||||LFL-7|L7||FJ.LF--LFJL7-|.LJ||LJ||||7LJ||LLL7|FJL7FJFJF-JF7F7F7F7L-77.|F|..FF||F----J|FJ|J|FJ-LJ-FL..|J|J-J-77L|.L|
J-|7.L-FFJ-|7F7F-JF-JFL-----LJLJ.LJLJJ7J|7.|L7FJ7-J|FJL77|||L7J.LJ7LF||L7FJL7L7L-7||||||||F-J7-J||F-JL|FL7F7F-J|FJLLJL-7J.7|F|7F|7F-7.L.||-L
JJLL7J7F||L-LJ|L7|L7-F7-|F7J.||J-|LL|FF7-7F-JLJ7L.LFJF7L7||L7|--JF7-FLJFJ|J.|FJJL||LJLJLJ||L|J7F|FJF|FJJLLJ||JFLJ||LL-7F77L--.|FJ-|-F|L-LFJ|
L7|LJ.FFJ|..|-J|L7LJ-LL-|-.FF-7F-J.F--JLL--7FL7FJ-F|FJL7|LJJLJ7|-LL-JJ|L7|JFLJJ|F||F77.||||777FFLJFLF77LFLLLJJL|7|7.L--FJF|-FLL|LLJ-JL7F|L-7
..|J77LJ-F7LF-7L-||-7LL|.FFLJ.|F7L-|J.77.--JJFF7|-L|||LLJ7|JFJ-J7.|JJ.77LJLL|FFF-JLJL7--F|L77JL7FLJ|J|7FFJ|-|7-F7LL.LJ-|.JJ.JJ--7.LLL7J--.-7
7-LFJ-J.||L7.F||FJF-|.L||-.|-JJL7||F7.F-7.FJFLJL7JLLJ-.L|-FJF-|.F-.L---LJ|.F77FL-7F-7|7LF|FJJ7||J|--.|LLL777LL7--J|FF|||.L|FJ.F---7..|L|.F|J
J..7-L7.---FJJJL7F--|7.LJ7F7||.F77-L7-L-7FF-|J77|7FLJJ7|F..|F--7|LJ-JJ7L7JF-J-F7L||.||-7-||JLLL7JF.|.|FLLJ.JJL|JJFL-7JF777|JJFJ.LLF7|L7J-FJ|
LF7.||||.|7..L||J|7FJ|.|JFL.LJFFFJ7JJ.L|L-L-J-F7J7F|F7-7|FF-|-|-7||.J.FJ|LJ.FLJJ|||-LJ.L7LJ-.L-LF7-FLJ7JLF7.|.||-F.7L-FJF7LL--77..F-F7||.L-.
.L.L-F|F|||FFFLJ.L-7JF-|--J7.7--J--J7--7FF7LFJLJ-F--||LJJJL||FL-FJL7|.7FL.|FL.F--||J.JFF7-JJF|7.|JF-7--7J||LF-F-7.JJFJ|.777..|.7JJJ.7LFL-|77
7JL|--JLL7.F-JJ.--|L--.|7-J.-JJJ.F---7-F-JL.J.L|-J-LJL-J-JLJ7..L|..L7-LL|----7J.LLJJ-LL-|.LFL7----J-LJL-FL-L-J|JJF-F|LJ7-JLLLJ-L.|JLJ.L|-LL.""".split("\n")

def test_input():
    return """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........""".split("\n")

class DIR(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

# Custom map populated with instances of the cell class
class Map:
    def __init__(self, map):
        self.map = self.generate_cells(map)
        self.start = self.find_start()
        self.create_links()

    def generate_cells(self, map):
        formatted = []
        for row_num, row in enumerate(map):
            formatted.append([])
            for symbol in row:
                formatted[row_num].append(Cell(symbol))
        return formatted
    
    # Generate each cell's list of traversable neighbors
    def create_links(self):
        for row, cells in enumerate(self.map):
            north = east = south = west = None

            for col, cell in enumerate(cells):
                north = None
                east = None
                south = None
                west = None
                try:
                    if(cell.can_north):
                        north = self.map[row-1][col]
                        if(north.symbol not in "|7F"):
                            north = None
                except:
                    pass
                try:
                    if(cell.can_east):
                        east = self.map[row][col+1]
                        if(east.symbol not in "J7-"):
                            east = None
                except:
                    pass
                try:
                    if(cell.can_south):
                        south = self.map[row+1][col]
                        if(south.symbol not in "|LJ"):
                            south = None
                except:
                    pass
                try:
                    if(cell.can_west):
                        west = self.map[row][col-1]
                        if(west.symbol not in "LF-"):
                            west = None
                except:
                    pass
                cell.neighbors = [north, east, south, west]

    # find the starting cell from the map of cells
    def find_start(self):
        for row in self.map:
            for cell in row:
                if(cell.symbol == "S"):
                    cell.can_north = True
                    cell.can_east = True
                    cell.can_south = True
                    cell.can_west = True
                    return cell
            
    # custom print function to view helpful data
    def print(self):
        for row in self.map:
            rowstr = ""
            for cell in row:
                if(cell.traversed):
                    # rowstr += str(cell.steps)
                    rowstr += "x"
                else:
                    rowstr += cell.symbol
            print(f"{rowstr}")
        print("\n") 

# Main cell class, which keeps track of traversable neighbors as well as its distance from start
class Cell:
    def __init__(self, symbol):
        self.symbol = symbol
        self.neighbors = None
        self.traversed = False
        self.can_north = False
        self.can_east = False
        self.can_south = False
        self.can_west = False
        self.steps = 0
        self.parent = None
        self.valid_directions()

    # determine which directions you can traverse from the cell given its symbol
    def valid_directions(self):
        match self.symbol:
            case "|":
                self.can_north = True
                self.can_south = True
            case "-":
                self.can_east = True
                self.can_west = True
            case "L":
                self.can_north = True
                self.can_east = True
            case "J":
                self.can_north = True
                self.can_west = True
            case "7":
                self.can_west = True
                self.can_south = True
            case "F":
                self.can_south = True
                self.can_east = True
            case ".":
                pass
        return

    # custom print function to display helpful data
    def print(self):
        print(f"Symbol: {self.symbol}\tNeighbors: {self.neighbors}\tTraversed: {self.traversed}")

# Main traverser class to find the path to the farthest point in the map
class Traverser:
    def __init__(self):
        self.map = None
        self.start = None
        self.stack = []
    
    # the main traverse function. no need to pass the map as the cells have all the needed data, map never modified, cells are changed
    def traverse(self, start):
        self.stack.append(start)
        max_steps = 0
        while(True):
            if(len(self.stack) == 0):
                return max_steps 
            steps = self.take_step(self.stack[-1], self.stack[-1].steps+1)
            if(steps > max_steps):
                max_steps = steps

    # function call to avoid maximum recursion depth being breached
    # this is the function that moves to the next possible cell in the map 
    def take_step(self, cell, steps):
        still_good = False
        # mark cell as traversed, this way it will never be added again
        cell.traversed = True
        for next_cell in cell.neighbors:
            if(next_cell is not None and not next_cell.traversed):
                # append all next next to traverse cells
                next_cell.steps = steps
                self.stack.append(next_cell)
                still_good = True
        # Cell has been fully explored, pop from the lifo queue
        if(not still_good):
            self.stack.pop()
        return steps

if __name__ == "__main__":
    m = Map(test_input())

    t = Traverser()
    max_distance = t.traverse(m.start)

    # print the final map
    m.print()

    if(max_distance % 2 == 1):
        max_distance = max_distance / 2 + 1
    else:
        max_distance /= 2

    print(round(max_distance))