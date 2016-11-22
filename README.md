# Operations

## Common Workflows

### Real Time Monitoring

### Node Information

The most basic way to get node information is to use `lsnodes`. This shows you a CSV formatted list of node information.

```
$ lsnodes
0000001e06200193,,,,10008
0000001e0620015e,,Single C1+ Started 2016-09-05,5th Floor Near Yongho,10012
0000001e0620026c,,,,10013
0000001e06200159,00F,AoT Chicago,ANL 5th Floor,10014
```

While this format is nice for integrating with other tools, it's not so easy to read. The `fmtnodes` command helps with this.

```
$ lsnodes | fmtnodes
ID           01e06200193
Name         <none>
Description  <none>
Location     <none>
Port         10008

ID           01e0620015e
Name         <none>
Description  Single C1+ Started 2016-09-05
Location     5th Floor Near Yongho
Port         10012
```

Now we can combine these with our other tools to make our life easier. For example, if I want to find all of the nodes containing "NIU", I can use.

```
$ lsnodes | grep -i niu | fmtnodes
```
