import re
punctuations = r'[.,!?;:()]'
date = r'\d{1,2}[-/]\d{1,2}[-/]\d{3,4}|\d{3,4}[-/]\d{1,2}[-/]\d{1,2}[-/]'
urls = r'https?://[^$\s/.?#].[^\s]'
email = r'[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z]{2,}'
number = r'(\d{1,3}(?:,\d{3})*(?:.\d{1,2})?)'
social_ids = r'@[a-zA-Z0-9_]+'
gujarati_text = r'[\u0A80-\u0AFF]+'
pattern = [punctuations,date,urls,email,number,social_ids,gujarati_text]
combined_pattern = '|'.join(pattern)
def tokenizer(text):
    tokens = []
    for patterns in pattern:
        matches = re.findall(patterns,text)
        tokens.extend(matches)
    return tokens
text = '''સ્વાગત છે! આજથી 15 માર્ચ 2025 થી, આપ અમારી નવી એપ્લિકેશન "Gujarati App" ડાઉનલોડ કરી શકો છો. આ એપ્લિકેશનનો લિંક છે: www.gujaratiapp.com

અમારા નવા ઓફર અને અપડેટ્સ માટે અમારો ફેસબુક પેજ ફોલો કરો: @gujaratiupdates
અને અમારો ટ્વિટર હેન્ડલ છે: @official_gujarati

યૂઝર ID: 67890, કૃપા કરીને તમારું લોગિન ID યાદ રાખો.

તમે તમારી પુછપરછ માટે અમારું ઇમેલ support@gujaratiapp.com પર પણ સંપર્ક કરી શકો છો.

કૃપા કરીને 15-03-2025 ના રોજ નવા અપડેટ વિશે વધુ માહિતી મેળવવા માટે અમારું વેબસાઇટ મુલાકાત લો.'''
tokens = tokenizer(text)
print(tokens)