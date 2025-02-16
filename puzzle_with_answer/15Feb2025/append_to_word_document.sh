#!/bin/bash
DTVAL="`date +'%d%b%Y'`"
echo "Starting consolidation of files for puzzles and it's answers for date -> $DTVAL"
cwd="`pwd`"
questions_outfile="${cwd}/word_puzzle_questions_${DTVAL}.doc"
answers_outfile="${cwd}/word_puzzle_answers_${DTVAL}.doc"
pzflag="`ls -l $cwd|egrep '^dr'|egrep puzzles|wc -l|sed 's/\s\+//g'`"
anflag="`ls -l $cwd|egrep '^dr'|egrep answers|wc -l|sed 's/\s\+//g'`"

#echo "gathered the flags pzflag:'${pzflag}', anflag:'${anflag}'"

if [[ "${pzflag// /}" == "1" ]]; then
	puzzle_filenames="`ls puzzles/puzzle*.txt|xargs`"
	#echo "puzzle questions -> $puzzle_filenames"
	for q_paper in ${puzzle_filenames}; do
		index="`basename $q_paper | cut -d'_' -f2 | cut -d'.' -f1`"
		echo "#################################################" >> $questions_outfile
		echo "$DTVAL Question Paper #${index}" >> $questions_outfile
		cat "${cwd}/${q_paper}" >> $questions_outfile
		echo "" >> $questions_outfile
		echo "" >> $questions_outfile
	done
fi

if [[ "${anflag// /}" == "1" ]]; then
	answer_filenames="`ls answers/answer*.txt|xargs`"
	#echo "puzzle answers -> $answer_filenames"
	for ans_sheet in ${answer_filenames}; do
		index="`basename $ans_sheet | cut -d'_' -f2 | cut -d'.' -f1`"
		echo "-------------------------------------------------" >> $answers_outfile
		echo "$DTVAL Answer Sheet #${index}" >> $answers_outfile
		cat "${cwd}/${ans_sheet}" >> $answers_outfile
		echo "" >> $answers_outfile
		echo "" >> $answers_outfile
	done
fi

test -f $questions_outfile
qoflag=$?
test -f $answers_outfile
aoflag=$?
if [[ "$qoflag" == "0" ]]; then
	echo "$DTVAL Questions file has been written -> $questions_outfile"
fi

if [[ "$aoflag" == "0" ]]; then
	echo "$DTVAL Answers file has been written -> $answers_outfile"
fi
