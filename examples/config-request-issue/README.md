To reproduce the issue, run 

1. ```poetry run pulumi up```

and follow the instructions to create a new stack. 

Add

2. ```pulumi config set example:value test```

to remove the error message. 

3. ```poetry run pulumi up```

should now run without problems. Finally, run

4. ```USE_PROVIDER=True pulumi up```

to reproduce the issue.