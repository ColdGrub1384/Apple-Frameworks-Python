'''
Classes from the 'ContactsAutocompleteUI' framework.
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

    
CNComposeDropTarget = _Class('CNComposeDropTarget')
CNComposeRecipients = _Class('CNComposeRecipients')
CNAutocompleteSearchManager = _Class('CNAutocompleteSearchManager')
CNAutocompleteContactsSearchTaskContext = _Class('CNAutocompleteContactsSearchTaskContext')
CNAutocompleteSupplementalGroup = _Class('CNAutocompleteSupplementalGroup')
CNAutocompleteSupplementalGroupMember = _Class('CNAutocompleteSupplementalGroupMember')
CNComposeAddressConcatenator = _Class('CNComposeAddressConcatenator')
CNAutocompleteFontMetricCache = _Class('CNAutocompleteFontMetricCache')
CNAutocompleteUIPreferences = _Class('CNAutocompleteUIPreferences')
CNComposeRecipient = _Class('CNComposeRecipient')
CNRecentComposeRecipient = _Class('CNRecentComposeRecipient')
CNComposeRecipientGroup = _Class('CNComposeRecipientGroup')
CNRecentComposeRecipientGroup = _Class('CNRecentComposeRecipientGroup')
CNUnifiedComposeRecipient = _Class('CNUnifiedComposeRecipient')
CNComposeRecipientOriginContext = _Class('CNComposeRecipientOriginContext')
CNComposeDragSource = _Class('CNComposeDragSource')
CNAtomCenteredTextAttachment = _Class('CNAtomCenteredTextAttachment')
CNAtomIcon = _Class('CNAtomIcon')
CNAutocompleteSearchOperation = _Class('CNAutocompleteSearchOperation')
CNContactsAutocompleteSearchOperation = _Class('CNContactsAutocompleteSearchOperation')
CNComposeHeaderView = _Class('CNComposeHeaderView')
CNComposeRecipientTextView = _Class('CNComposeRecipientTextView')
CNModernAtomBackgroundView = _Class('CNModernAtomBackgroundView')
CNModernAtomIconView = _Class('CNModernAtomIconView')
CNAtomView = _Class('CNAtomView')
CNComposeRecipientAtom = _Class('CNComposeRecipientAtom')
CNComposeTableViewCell = _Class('CNComposeTableViewCell')
CNComposeRecipientTableViewCell = _Class('CNComposeRecipientTableViewCell')
CNAutocompleteDisambiguatingTableViewCell = _Class('CNAutocompleteDisambiguatingTableViewCell')
CNAutocompleteResultsTableView = _Class('CNAutocompleteResultsTableView')
CNComposeHeaderLabelView = _Class('CNComposeHeaderLabelView')
CNAtomTextView = _Class('CNAtomTextView')
CNChevronButton = _Class('CNChevronButton')
CNComposeRecipientActionButton = _Class('CNComposeRecipientActionButton')
CNAutocompleteResultsTableViewController = _Class('CNAutocompleteResultsTableViewController')
CNAutocompleteGroupDetailViewController = _Class('CNAutocompleteGroupDetailViewController')
