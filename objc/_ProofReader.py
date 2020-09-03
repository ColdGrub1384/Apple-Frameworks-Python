'''
Classes from the 'ProofReader' framework.
'''

try:
    from rubicon.objc import ObjCClass
except ValueError:
    def ObjCClass(name):
        return None


def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None

    
PRAutocorrectionContext = _Class('PRAutocorrectionContext')
PRPinyinContext = _Class('PRPinyinContext')
PRZhuyinContext = _Class('PRZhuyinContext')
PRModification = _Class('PRModification')
PRPinyinModification = _Class('PRPinyinModification')
PRZhuyinModification = _Class('PRZhuyinModification')
PRTurkishSuffix = _Class('PRTurkishSuffix')
PRLexicon = _Class('PRLexicon')
PRLexiconCursor = _Class('PRLexiconCursor')
PRLexiconCompletion = _Class('PRLexiconCompletion')
PRLexiconCorrection = _Class('PRLexiconCorrection')
PRLexiconCorrectionCursor = _Class('PRLexiconCorrectionCursor')
PRLanguage = _Class('PRLanguage')
PRCandidateList = _Class('PRCandidateList')
PRCandidate = _Class('PRCandidate')
PRErrorModel = _Class('PRErrorModel')
PRRecordedCorrection = _Class('PRRecordedCorrection')
PRTypologyRecord = _Class('PRTypologyRecord')
PRTypologyCandidate = _Class('PRTypologyCandidate')
PRTypologyCorrection = _Class('PRTypologyCorrection')
PRDictionary = _Class('PRDictionary')
PRLanguageModel = _Class('PRLanguageModel')
AppleSpell = _Class('AppleSpell')
PRPinyinString = _Class('PRPinyinString')
