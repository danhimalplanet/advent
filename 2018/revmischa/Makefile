.PHONY: new

DAY=$(shell python -c "import aoc; print(aoc.current_day)")
TARGET="aoc/day$(DAY)"

# make new day
new: $(TARGET)
	find $(TARGET) -type f -exec perl -p -i -e "s/dayN/day$(DAY)/" {} \;
	find $(TARGET) -type f -exec perl -p -i -e "s/DayN/Day$(DAY)/" {} \;
	mv $(TARGET)/test_dayN.py $(TARGET)/test_day$(DAY).py
$(TARGET):
	cp -r aoc/template $(TARGET)


part1:
	pytest -s -ff $(TARGET)/test_day$(DAY).py
