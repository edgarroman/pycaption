#!/usr/bin/python
# -*- coding: utf-8 -*-

from pycaption import BaseReader

COMMANDS = {
    '9420': '',
    '9429': '',
    '9425': '',
    '9426': '',
    '94a7': '',
    '942a': '',
    '94ab': '',
    '942c': '',
    '94ae': '',
    '942f': '',
    '9140': '',
    '91c1': '',
    '91c2': '',
    '9143': '',
    '91c4': '',
    '9145': '',
    '9146': '',
    '91c7': '',
    '91c8': '',
    '9149': '',
    '914a': '',
    '91cb': '',
    '914c': '',
    '91cd': '',
    '91ce': '',
    '914f': '',
    '91d0': '',
    '9151': '',
    '9152': '',
    '91d3': '',
    '9154': '',
    '91d5': '',
    '91d6': '',
    '9157': '',
    '9158': '',
    '91d9': '',
    '91da': '',
    '915b': '',
    '91dc': '',
    '915d': '',
    '915e': '',
    '91df': '',
    '91e0': '',
    '9161': '',
    '9162': '',
    '91e3': '',
    '9164': '',
    '91e5': '',
    '91e6': '',
    '9167': '',
    '9168': '',
    '91e9': '',
    '91ea': '',
    '916b': '',
    '91ec': '',
    '916d': '',
    '916e': '',
    '91ef': '',
    '9170': '',
    '91f1': '',
    '91f2': '',
    '9173': '',
    '91f4': '',
    '9175': '',
    '9176': '',
    '91f7': '',
    '91f8': '',
    '9179': '',
    '917a': '',
    '91fb': '',
    '91fc': '',
    '91fd': '',
    '91fe': '',
    '917f': '',
    '9240': '',
    '92c1': '',
    '92c2': '',
    '9243': '',
    '92c4': '',
    '9245': '',
    '9246': '',
    '92c7': '',
    '92c8': '',
    '9249': '',
    '924a': '',
    '92cb': '',
    '924c': '',
    '92cd': '',
    '92ce': '',
    '924f': '',
    '92d0': '',
    '9251': '',
    '9252': '',
    '92d3': '',
    '9254': '',
    '92d5': '',
    '92d6': '',
    '9257': '',
    '9258': '',
    '92d9': '',
    '92da': '',
    '925b': '',
    '92dc': '',
    '925d': '',
    '925e': '',
    '92df': '',
    '92e0': '',
    '9261': '',
    '9262': '',
    '92e3': '',
    '9264': '',
    '92e5': '',
    '92e6': '',
    '9267': '',
    '9268': '',
    '92e9': '',
    '92ea': '',
    '926b': '',
    '92ec': '',
    '926d': '',
    '926e': '',
    '92ef': '',
    '9270': '',
    '92f1': '',
    '92f2': '',
    '9273': '',
    '92f4': '',
    '9275': '',
    '9276': '',
    '92f7': '',
    '92f8': '',
    '9279': '',
    '927a': '',
    '92fb': '',
    '92fc': '',
    '92fd': '',
    '92fe': '',
    '927f': '',
    '1540': '',
    '15c1': '',
    '15c2': '',
    '1543': '',
    '15c4': '',
    '1545': '',
    '1546': '',
    '15c7': '',
    '15c8': '',
    '1549': '',
    '154a': '',
    '15cb': '',
    '154c': '',
    '15cd': '',
    '15ce': '',
    '154f': '',
    '15d0': '',
    '1551': '',
    '1552': '',
    '15d3': '',
    '1554': '',
    '15d5': '',
    '15d6': '',
    '1557': '',
    '1558': '',
    '15d9': '',
    '15da': '',
    '155b': '',
    '15dc': '',
    '155d': '',
    '155e': '',
    '15df': '',
    '15e0': '',
    '1561': '',
    '15462': '',
    '15e3': '',
    '1564': '',
    '15e5': '',
    '15e6': '',
    '1567': '',
    '1568': '',
    '15e9': '',
    '15ea': '',
    '156b': '',
    '15ec': '',
    '156d': '',
    '156e': '',
    '15ef': '',
    '1570': '',
    '15f1': '',
    '15f2': '',
    '1573': '',
    '15f4': '',
    '1575': '',
    '1576': '',
    '15f7': '',
    '15f8': '',
    '1579': '',
    '157a': '',
    '15fb': '',
    '15fc': '',
    '15fd': '',
    '15fe': '',
    '157f': '',
    '1640': '',
    '16c1': '',
    '16c2': '',
    '1643': '',
    '16c4': '',
    '1645': '',
    '1646': '',
    '16c7': '',
    '16c8': '',
    '1649': '',
    '164a': '',
    '16cb': '',
    '164c': '',
    '16cd': '',
    '16ce': '',
    '164f': '',
    '16d0': '',
    '1651': '',
    '1652': '',
    '16d3': '',
    '1654': '',
    '16d5': '',
    '16d6': '',
    '1657': '',
    '1658': '',
    '16d9': '',
    '16da': '',
    '165b': '',
    '16dc': '',
    '165d': '',
    '165e': '',
    '16df': '',
    '16e0': '',
    '1661': '',
    '16462': '',
    '16e3': '',
    '1664': '',
    '16e5': '',
    '16e6': '',
    '1667': '',
    '1668': '',
    '16e9': '',
    '16ea': '',
    '166b': '',
    '16ec': '',
    '166d': '',
    '166e': '',
    '16ef': '',
    '1670': '',
    '16f1': '',
    '16f2': '',
    '1673': '',
    '16f4': '',
    '1675': '',
    '1676': '',
    '16f7': '',
    '16f8': '',
    '1679': '',
    '167a': '',
    '16fb': '',
    '16fc': '',
    '16fd': '',
    '16fe': '',
    '167f': '',
    '9740': '',
    '97c1': '',
    '97c2': '',
    '9743': '',
    '97c4': '',
    '9745': '',
    '9746': '',
    '97c7': '',
    '97c8': '',
    '9749': '',
    '974a': '',
    '97cb': '',
    '974c': '',
    '97cd': '',
    '97ce': '',
    '974f': '',
    '97d0': '',
    '9751': '',
    '9752': '',
    '97d3': '',
    '9754': '',
    '97d5': '',
    '97d6': '',
    '9757': '',
    '9758': '',
    '97d9': '',
    '97da': '',
    '975b': '',
    '97dc': '',
    '975d': '',
    '975e': '',
    '97df': '',
    '97e0': '',
    '9761': '',
    '9762': '',
    '97e3': '',
    '9764': '',
    '97e5': '',
    '97e6': '',
    '9767': '',
    '9768': '',
    '97e9': '',
    '97ea': '',
    '976b': '',
    '97ec': '',
    '976d': '',
    '976e': '',
    '97ef': '',
    '9770': '',
    '97f1': '',
    '97f2': '',
    '9773': '',
    '97f4': '',
    '9775': '',
    '9776': '',
    '97f7': '',
    '97f8': '',
    '9779': '',
    '977a': '',
    '97fb': '',
    '97fc': '',
    '97fd': '',
    '97fe': '',
    '977f': '',
    '1040': '',
    '10c1': '',
    '10c2': '',
    '1043': '',
    '10c4': '',
    '1045': '',
    '1046': '',
    '10c7': '',
    '10c8': '',
    '1049': '',
    '104a': '',
    '10cb': '',
    '104c': '',
    '10cd': '',
    '10ce': '',
    '104f': '',
    '10d0': '',
    '1051': '',
    '1052': '',
    '10d3': '',
    '1054': '',
    '10d5': '',
    '10d6': '',
    '1057': '',
    '1058': '',
    '10d9': '',
    '10da': '',
    '105b': '',
    '10dc': '',
    '105d': '',
    '105e': '',
    '10df': '',
    '1340': '',
    '13c1': '',
    '13c2': '',
    '1343': '',
    '13c4': '',
    '1345': '',
    '1346': '',
    '13c7': '',
    '13c8': '',
    '1349': '',
    '134a': '',
    '13cb': '',
    '134c': '',
    '13cd': '',
    '13ce': '',
    '134f': '',
    '13d0': '',
    '1351': '',
    '1352': '',
    '13d3': '',
    '1354': '',
    '13d5': '',
    '13d6': '',
    '1357': '',
    '1358': '',
    '13d9': '',
    '13da': '',
    '135b': '',
    '13dc': '',
    '135d': '',
    '135e': '',
    '13df': '',
    '13e0': '',
    '1361': '',
    '13462': '',
    '13e3': '',
    '1364': '',
    '13e5': '',
    '13e6': '',
    '1367': '',
    '1368': '',
    '13e9': '',
    '13ea': '',
    '136b': '',
    '13ec': '',
    '136d': '',
    '136e': '',
    '13ef': '',
    '1370': '',
    '13f1': '',
    '13f2': '',
    '1373': '',
    '13f4': '',
    '1375': '',
    '1376': '',
    '13f7': '',
    '13f8': '',
    '1379': '',
    '137a': '',
    '13fb': '',
    '13fc': '',
    '13fd': '',
    '13fe': '',
    '137f': '',
    '9440': '',
    '94c1': '',
    '94c2': '',
    '9443': '',
    '94c4': '',
    '9445': '',
    '9446': '',
    '94c7': '',
    '94c8': '',
    '9449': '',
    '944a': '',
    '94cb': '',
    '944c': '',
    '94cd': '',
    '94ce': '',
    '944f': '',
    '94d0': '',
    '9451': '',
    '9452': '',
    '94d3': '',
    '9454': '',
    '94d5': '',
    '94d6': '',
    '9457': '',
    '9458': '',
    '94d9': '',
    '94da': '',
    '945b': '',
    '94dc': '',
    '945d': '',
    '945e': '',
    '94df': '',
    '94e0': '',
    '9461': '',
    '9462': '',
    '94e3': '',
    '9464': '',
    '94e5': '',
    '94e6': '',
    '9467': '',
    '9468': '',
    '94e9': '',
    '94ea': '',
    '946b': '',
    '94ec': '',
    '946d': '',
    '946e': '',
    '94ef': '',
    '9470': '',
    '94f1': '',
    '94f2': '',
    '9473': '',
    '94f4': '',
    '9475': '',
    '9476': '',
    '94f7': '',
    '94f8': '',
    '9479': '',
    '947a': '',
    '94fb': '',
    '94fc': '',
    '94fd': '',
    '94fe': '',
    '947f': '',
    '97a1': '',
    '97a2': '',
    '9723': '',
    '94a1': '',
    '94a4': '',
    '94ad': '',
    '1020': '',
    '10a1': '',
    '10a2': '',
    '1023': '',
    '10a4': '',
    '1025': '',
    '1026': '',
    '10a7': '',
    '10a8': '',
    '1029': '',
    '102a': '',
    '10ab': '',
    '102c': '',
    '10ad': '',
    '10ae': '',
    '102f': '',
    '97ad': '',
    '97a4': '',
    '9725': '',
    '9726': '',
    '97a7': '',
    '97a8': '',
    '9729': '',
    '972a': '',
    '9120': '',
    '91a1': '',
    '91a2': '',
    '9123': '',
    '91a4': '',
    '9125': '',
    '9126': '',
    '91a7': '',
    '91a8': '',
    '9129': '',
    '912a': '',
    '91ab': '',
    '912c': '',
    '91ad': '',
    '97ae': '',
    '972f': '',
    '91ae': '',
    '912f': '',
    '94a8': '',
    '9423': '',
    '94a2': '',
}

CHARACTERS = {
    '20': ' ',
    'a1': '!',
    'a2': '"',
    '23': '#',
    'a4': '$',
    '25': '%',
    '26': '&',
    'a7': '\'',
    'a8': '(',
    '29': ')',
    '2a': 'á',
    'ab': '+',
    '2c': ',',
    'ad': '-',
    'ae': '.',
    '2f': '/',
    'b0': '0',
    '31': '1',
    '32': '2',
    'b3': '3',
    '34': '4',
    'b5': '5',
    'b6': '6',
    '37': '7',
    '38': '8',
    'b9': '9',
    'ba': ':',
    '3b': ';',
    'bc': '<',
    '3d': '=',
    '3e': '>',
    'bf': '?',
    '40': '@',
    'c1': 'A',
    'c2': 'B',
    '43': 'C',
    'c4': 'D',
    '45': 'E',
    '46': 'F',
    'c7': 'G',
    'c8': 'H',
    '49': 'I',
    '4a': 'J',
    'cb': 'K',
    '4c': 'L',
    'cd': 'M',
    'ce': 'N',
    '4f': 'O',
    'd0': 'P',
    '51': 'Q',
    '52': 'R',
    'd3': 'S',
    '54': 'T',
    'd5': 'U',
    'd6': 'V',
    '57': 'W',
    '58': 'X',
    'd9': 'Y',
    'da': 'Z',
    '5b': '[',
    'dc': 'é',
    '5d': ']',
    '5e': 'í',
    'df': 'ó',
    'e0': 'ú',
    '61': 'a',
    '62': 'b',
    'e3': 'c',
    '64': 'd',
    'e5': 'e',
    'e6': 'f',
    '67': 'g',
    '68': 'h',
    'e9': 'i',
    'ea': 'j',
    '6b': 'k',
    'ec': 'l',
    '6d': 'm',
    '6e': 'n',
    'ef': 'o',
    '70': 'p',
    'f1': 'q',
    'f2': 'r',
    '73': 's',
    'f4': 't',
    '75': 'u',
    '76': 'v',
    'f7': 'w',
    'f8': 'x',
    '79': 'y',
    '7a': 'z',
    'fb': 'ç',
    '7c': '',
    'fd': 'Ñ',
    'fe': 'ñ',
    '7f': '',
    '80': ' '
}

SPECIAL_CHARS = {
    '91b0': '®',
    '9131': '°',
    '9132': '½',
    '91b3': '¿',
    '91b4': '™',
    '91b5': '¢',
    '91b6': '£',
    '9137': u"\u266A",
    '9138': 'à',
    '91b9': ' ',
    '91ba': 'è',
    '913b': 'â',
    '91bc': 'ê',
    '913d': 'î',
    '913e': 'ô',
    '91bf': 'û',
    
    '9220': 'Á',
    '92a1': 'É',
    '92a2': 'Ó',
    '9223': 'Ú',
    '92a4': 'Ü',
    '9225': 'ü',
    '9226': '‘',
    '92a7': '¡',
    '92a8': '*',
    '9229': '’',
    '922a': '—',
    '92ab': '©',
    '922c': '',
    '92ad': '•',
    '92ae': '“',
    '922f': '”',
    '92b0': 'À',
    '9231': 'Â',
    '9232': 'Ç',
    '92b3': 'È',
    '9234': 'Ê',
    '92b5': 'Ë',
    '92b6': 'ë',
    '9237': 'Î',
    '9238': 'Ï',
    '92b9': 'ï',
    '92ba': 'Ô',
    '923b': 'Ù',
    '92bc': 'ù',
    '923d': 'Û',
    '923e': '«',
    '92bf': '»',
    '1320': 'Ã',
    '13a1': 'ã',
    '13a2': 'Í',
    '1323': 'Ì',
    '13a4': 'ì',
    '1325': 'Ò',
    '1326': 'ò',
    '13a7': 'Õ',
    '13a8': 'õ',
    '1329': '{',
    '132a': '}',
    '13ab': '\\',
    '132c': '^',
    '13ad': '_',
    '13ae': '¦',
    '132f': '~',
    '13b0': 'Ä',
    '1331': 'ä',
    '1332': 'Ö',
    '13b3': 'ö',
    '1334': 'ß',
    '13b5': '¥',
    '13b6': '¤',
    '1337': '|',
    '1338': 'Å',
    '13b9': 'å',
    '13ba': 'Ø',
    '133b': 'ø',
    '13bc': '',
    '133d': '',
    '133e': '',
    '13bf': '',
}

class SCCReader(BaseReader):
    def read(self, content, lang='en'):
        inlines = content.splitlines()
        scc = []
        for line in inlines:
            if line == inlines[0]:
                scc.append(line)
                continue
            if line.strip() == '':
                continue
                
            line = line.replace(';', ':')
            
            parts = line.split('	')
            caption = ''
            time = parts[0]
            scc.append("TIME: %s" % time)
            for word in parts[1].split(' '):
                if word.strip() == '':
                    continue
                if word in COMMANDS:
                    caption += COMMANDS[word]
                elif word in SPECIAL_CHARS:
                    caption += SPECIAL_CHARS[word]
                else:
                    byte1 = word[:2]
                    byte2 = word[2:]
                    if byte1 in CHARACTERS:
                        caption += CHARACTERS[byte1]
                        if byte2 in CHARACTERS:
                            caption += CHARACTERS[byte2]
                        else:
                            caption -= CHARACTERS[byte1]
            scc.append(' '.join(caption.split()))
        return '\n'.join(scc)
                        
                        
        