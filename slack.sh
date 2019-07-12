branch=$1
test_name=$2
requests=$3
message_color="#36a64f"

slack_message (){
    url='https:''
    username=''

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
