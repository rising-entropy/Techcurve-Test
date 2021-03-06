# Techcurve Test

Required Python Libraries can be found in requirements.txt.

#### How to launch the server:
In the directory on level of manage.py<br>
<code>python manage.py runserver</code>

## API End-Points:

### Authentication
<code>api/login/</code> For Login, Returns the Token (We are using Knox Authentication.)<br>
<code>api/logout/</code> For Logout.

##### For every API henceforth (also the Logout, we'd be sharing a Header as Key: Authorization, Value: Token {{token}} ).

### CRUD on the Models

For all the 4 models, we can perform CRUD with the following endpoints:
- <code><strong>GET</strong> viewset/revenues/</code> Fetch the list of all Revenue Instances
- <code><strong>POST</strong> viewset/revenues/</code> Create a Revenue Instance
- <code><strong>GET</strong> viewset/revenues/<int:id></code> Fetch Revenue Instance with specified `id`
- <code><strong>PUT</strong> viewset/revenues/<int:id></code> Update Revenue Instance with specified `id`
- <code><strong>DELETE</strong> viewset/revenues/<int:id></code> Delete Revenue Instance with specified `id`

Similar Schema would be used for `expenses`, `bankbalance` and `invoice` as;
- `viewset/expenses/`
- `viewset/bankbalance/`
- `viewset/invoice/`

### Required Custom APIs:

##### Get the Latest Bank Balance
`GET api/currentbankbalance/`

##### Get the Current Profit-Loss
`GET api/profitloss/`

##### Get Total Expenses
`GET api/expense/`

##### Get Total Revenue
`GET api/revenue/`

##### Get Profit Loss Data for past 12 Months for the Graph.
`GET api/profitlossgraph/`

##### Get Profit Loss Data for past 12 Months for the Graph.
`GET api/profitlossgraph/`
