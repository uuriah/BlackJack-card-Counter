import PySimpleGUI as sg
sg.theme('DarkBlue14')
sg.set_options(font = ("Arial Bold", 14))

toprow = ['2,3,4,5,6', '7,8,9', '10,J,Q,K,A']
rows = [[1, 0, -1]]
tbl1 = sg.Table(values =rows, headings =toprow,
  auto_size_columns = False,
  hide_vertical_scroll=True,
  def_col_width= 5,
  num_rows = 1,
  display_row_numbers = False,
  justification ='center',
  enable_events = False,
  expand_x = True, expand_y = True,
  enable_click_events = False)

layout = [
[sg.Text("--Card Value Key--")],
[tbl1],
[sg.Text("Enter the total number of decks:     "),sg.Input(key='-DECKS-',size = (3,1)),sg.Button("Decks")],
[sg.Text("Enter the total count for this hand:                  "),sg.Input(key='-COUNT-', size = (3,1))],          
[sg.Text("Enter the amount of cards played this hand:   "),sg.InputText(key = '-CARDS-', size = (3,1))],    
[sg.Text("Enter the amount of -1 value cards this hand: "),sg.InputText(key = '-NEGCARDS-',size = (3,1))],
[sg.Text("                                      "),sg.Button("Update")],
[sg.Text("Cards Remaining: "),sg.Text(key = 'num_Cards',size = (5,1))],
[sg.Text("Current Count: "),sg.Text(key = 'count_Out', size = (5,1))],
[sg.Text("True Count: "),sg.Text(key='true_Count',size = (5,1))],
[sg.Text("Total Cards Played: "), sg.Text(key = 'cards_Out', size = (5,1))],

[sg.Text("%Chance top card is value 10 or Ace"),sg.ProgressBar(100, orientation = 'h', expand_y=True, size=(20,20), key = '-PBAR-'),sg.Text('',key = '-PCHANCE-', enable_events=True, justification='center',expand_x=True)],
[sg.Button("Shuffle"), sg.Button("Quit")]]


#some variables
numDecks = 0
currentCount = 0
cardsPlayed = 0
cardsRemain =0
trueCount = 0
totalNegCards = 0
chanceTopDeck = 0

#creating the window
window = sg.Window("  BlackJack Card Counter", layout, margins=(15,15), button_color='gray')


while True:
    event, values = window.read()
 
    if event == 'Decks':
      numDecks = int(values['-DECKS-'])
      cardsRemain = 52*numDecks
      totalNegCards = 20*numDecks
      chanceTopDeck = round((totalNegCards/cardsRemain)*100,2)
      window['num_Cards'].update(cardsRemain)
      window['-PBAR-'].update(chanceTopDeck)
      window['-PCHANCE-'].update(chanceTopDeck)
      
    if event == 'Update':
      if values['-COUNT-'] =='':
        values['-COUNT-'] =0
      else:
        currentCount = currentCount + int(values['-COUNT-']) 
        window['count_Out'].update(currentCount)
        window['-COUNT-']('')
        trueCount = round(currentCount/numDecks,2)
        window['true_Count'].update(trueCount)
      if values['-CARDS-'] =='' or int(values['-CARDS-']) < 0:
        values['-CARDS-'] =0
        window['-CARDS-']('')
      else:
        cardsPlayed += int(values['-CARDS-'])
        window['cards_Out'].update(cardsPlayed)
        cardsRemain -= int(values['-CARDS-'])
        window['num_Cards'].update(cardsRemain)
        window['-CARDS-']('')
      if values['-NEGCARDS-'] == '' or int(values['-NEGCARDS-']) < 0:
        values['-NEGCARDS-'] =0
        window['-NEGCARDS-']('')
      else:
        totalNegCards -= int(values['-NEGCARDS-'])
        window['-NEGCARDS-']('')
        chanceTopDeck =     round((totalNegCards/cardsRemain)*100,2)
        window['-PBAR-'].update(chanceTopDeck)
        window['-PCHANCE-'].update(chanceTopDeck)

    if event == "Shuffle":
      cardsRemain = 52*numDecks
      totalNegCards = 20*numDecks
      chanceTopDeck = round((totalNegCards/cardsRemain)*100,2)
      window['num_Cards'].update(cardsRemain)
      window['-PBAR-'].update(chanceTopDeck)
      window['-PCHANCE-'].update(chanceTopDeck)
      currentCount = 0
      cardsPlayed = 0
      window['count_Out'].update(currentCount)
      window['true_Count'].update(currentCount)
      window['cards_Out'].update('')
  
    if event == "Quit" or event == sg.WIN_CLOSED:
        break

window.close()
