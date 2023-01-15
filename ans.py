from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            x=dict(type='int', required=True),
            y=dict(type='int', required=True),
        ),
    )

    x = module.params['x']
    y = module.params['y']

    sum = x + y

    module.exit_json(changed=False, sum=sum)

if __name__ == '__main__':
    main()
