def add_time(start,add,day=None):
  time, period = start.split()
  hour, minutes = map(int,time.split(':')) # converting everything to int
  addH, addM = map(int,add.split(':'))
  midday = ('PM','AM')
  new_day = ''
  later = ''

  # Clockwork:
  # These calculations essentially do the math for capping minutes to 59 and hours to 12
  # Divmod and tuple assigment!
  carry, minutes = divmod(minutes + addM,60) # 'carry' is 1 (minutes >= 60) or 0 (minutes <= 59)
  hour += carry
  cycles, hour = divmod(hour + addH,12) # 'cycles' is # of 12-hours (half days) that 'hour' exceeds

  # AM or PM:
  # We can also think of 'cycles' as the # of switches between AM and PM, this means that an even number of switches doesn't change the period but an odd number will
  # Use this logic to subtract 1(odd cycles) or 0(even cycles) from the current period
  period = abs(midday.index(period)-(cycles % 2)) # period is an index in midday
  passed = (period + cycles) // 2  # 'passed' describes the number of days passed

  if hour == 0: # basically an edge case created from my modulus calculations
    hour = 12

  if minutes < 10: # standardizing time format, 12:1 -> 12:01
    minutes = f'0{minutes}'

  # Day of Week:
  # In one line, we can determine what the current day of the week is by index, add the number of days passed, and get the new day of the week
  # The modulus operation will scale the new day, so day 10 -> day 3, day 145 -> day 5, etc.
  if day:
      week = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
      new_day = f', {week[(week.index(day.capitalize()) + passed) % 7]}'

  # Just some string formatting
  if passed == 1:
      later = ' (next day)'
  elif passed != 0:
      later = f' ({passed} days later)'

  return f'{hour}:{minutes} {midday[period]}{new_day}{later}'
