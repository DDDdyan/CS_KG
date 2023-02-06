export const fakeMessages = [
  {
  'type': 'text',
  'text': 'Hello. Have a nice day!',
  'disableInput': false
},
{
  'type': 'button',
  'text': 'How can we help you today?',
  'options': [
  {
    'text': 'Search Suport Articles',
    'value': 'search',
    'action': 'postback'
  },
  {
    'text': 'Submit Support Technology',
    'value': 'submit_ticket',
    'action': 'postback'
  }
],
  'disableInput': true
},
{
  'type': 'text',
  'text': 'Please type your problem',
  'disableInput': false
},
{
  'type': 'button',
  'text': 'Here are the results from our knowledgebase.',
  'options': [
  {
    'text': 'How to create a menu',
    'value': 'https://google.com',
    'action': 'url'
  },
  {
    'text': 'How to add a submenu to a menu',
    'value': 'https://google.com',
    'action': 'url'
  },
  {
    'text': "Not what I'm looking for",
    'value': 'result_not_match',
    'action': 'postback'
  }
],
  'disableInput': true
},
{
  'type': 'text',
  'text': 'Sorry to hear that.',
  'disableInput': false
},
{
  'type': 'button',
  'text': 'All done! .',
  'options': [
  {
    'text': 'View ppt',
    'value': 'https://google.com',
    'action': 'url'
  }
],
  'disableInput': false
}
]
