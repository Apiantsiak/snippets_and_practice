from typing import Dict, List

EMAILS: Dict[str, List[str]] = {
	'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']
}

print(*sorted({name + '@' + key for key, value in EMAILS.items() for name in value}), sep='\n')
