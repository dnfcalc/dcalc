import json
import os
import sys


def _fail(message: str) -> None:
    print(json.dumps({'error': message}, ensure_ascii=False))
    sys.exit(1)


def _parse_args() -> tuple[str, str, str, str]:
    if len(sys.argv) < 5:
        _fail('usage: python_bridge.py <project_root> <command> <alter> <equ_version>')
    project_root = sys.argv[1]
    command = sys.argv[2]
    alter = sys.argv[3]
    equ_version = sys.argv[4]
    return project_root, command, alter, equ_version


def _ensure_path(project_root: str) -> None:
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    sys.argv[0] = os.path.join(project_root, 'main.py')
    os.chdir(project_root)


def _load_character(alter: str, equ_version: str):
    from core.basic.character import createCharacter

    character = createCharacter(alter, equ_version or '0')
    if character is None:
        raise RuntimeError(f'failed to create character for {alter}')
    return character


def _character_info(alter: str, equ_version: str):
    character = _load_character(alter, equ_version)
    return character.getInfo()


def _character_skills(alter: str, equ_version: str):
    info = _character_info(alter, equ_version)
    skills = info.get('skills', [])
    return [
        {
            'id': str(skill.get('id', '')),
            'name': skill.get('name', ''),
            'type': skill.get('type', ''),
            'learnLv': int(skill.get('learnLv', 0)),
            'maxLearnLv': int(skill.get('maxLearnLv', 0)),
            'hasVP': bool(skill.get('hasVP', False)),
            'hasUP': bool(skill.get('hasUP', False)),
            'uuid': skill.get('uuid', ''),
        }
        for skill in skills
    ]


def main() -> None:
    project_root, command, alter, equ_version = _parse_args()
    _ensure_path(project_root)

    try:
        if command == 'character-info':
            data = _character_info(alter, equ_version)
        elif command == 'character-skills':
            data = _character_skills(alter, equ_version)
        else:
            _fail(f'unknown command: {command}')
        print(json.dumps(data, ensure_ascii=False))
    except Exception as ex:
        _fail(str(ex))


if __name__ == '__main__':
    main()
