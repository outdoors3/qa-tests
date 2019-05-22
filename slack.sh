branch=$1
test_name=$2
requests=$3
message_color="#36a64f"

slack_message (){
    url='https://hooks.slack.com/services/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'
    username='zabbix'

    to="#qa-bots"
    subject="INFO"

    read -d '' payload << EOF
    {
            "channel": "${to}",
            "username": "${username}",
            "attachments": [
            {
                "fallback": "",
                "text": "${message}",
                "fields": [
                    {
                        "title": "Branch: $branch",
                        "value": "${test_url}",
                        "short": true
                    },
                ],
                "color": "$message_color"
            }
        ]
    }
EOF
curl -m 5 --data "${payload}" -H 'Content-type: application/json' $url
}


if [[ $test_name != "jmeter" ]]
then 
    test_failed=$(grep -c Failed result.txt)
    if [[ $test_failed -ne 0 ]]
    then
         message_color="#F35A00"
         message=$(cat result.txt)
         session_id=$(cat session_id.txt)
         test_url=""
         slack_message
    else 
        message=$(cat result.txt)
        session_id=$(cat session_id.txt)
        test_url=""
        slack_message
    fi
else 
    message="Results of load test on 38 pages, $requests requests for each page:"
    test_url=""
    slack_message
fi