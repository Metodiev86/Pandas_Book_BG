

import pandas as pd

# Примерен Series с имейл адреси
emails = pd.Series([
    'ivan@example.com',
    'maria@domain.bg',
    'peter@company.org'
])

# Извличане на домейн името (частта след '@')
domains = emails.str.split('@').str[1]

print(domains)
