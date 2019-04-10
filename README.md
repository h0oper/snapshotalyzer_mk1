# snapshotalyzer_mk1

Demo project to manage AWS EC2 instance snapshots.

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

Guru uses the configuration file created by the AWS cli e.g.

'aws configrue --profile guru'

## Running

'pipenv run python guru/guru.py <command> <subcommand> <--project=PROJECTNAME>'

*command* is instance, volumes, or snapshots
*subcommand* depends on command
*project* is optional