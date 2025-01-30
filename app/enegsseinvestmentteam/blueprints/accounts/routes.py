{% extends "base.html" %}

{% block content %}
<nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm mb-4">
    <div class="container-fluid">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">

                <li class="nav-item">
                    <a class="nav-link" href="#payments">Payments</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="#users">Users</a>
                </li>
                
                <li class="nav-item">
                    <a class="nav-link" href="#transactions">Transactions</a>
                </li>
                
                <li class="nav-item">
                    {% if current_user.is_authenticated %}
                    <a class="nav-link text-danger" href="{{ url_for('accounts.logout') }}">Logout</a>
                    {% else %}
                    <a class="nav-link text-danger" href="{{ url_for('accounts.login') }}">Login</a>
                    {% endif %}
                </li>
            </ul>
        </div>
    </div>
</nav>
<div class="container mt-5">
    <h2 class="mb-4 text-center text-success">Admin Dashboard</h2>

    <!-- Section 1: Add Payment Method -->
    <div class="card mb-4 shadow-sm border-0">
        <div class="card-header bg-success text-white">
            <h3 class="mb-0">Add Payment Method</h3>
        </div>
        <div class="card-body">
            <form method="POST" action="{{ url_for('accounts.add_payment_method') }}">
                <div class="mb-3">
                    <label for="method_type" class="form-label">Payment Method Type</label>
                    <select id="method_type" name="method_type" class="form-select" onchange="toggleMethodFields()" required>
                        <option value="" disabled selected>Select</option>
                        <option value="Bank Transfer">Bank Transfer</option>
                        <option value="Cryptocurrency">Cryptocurrency</option>
                    </select>
                </div>
            
                <!-- Bank Transfer Fields -->
                <div id="bank_fields" class="mt-3" style="display: none;">
                    <div class="mb-3">
                        <label for="account_number" class="form-label">Account Number</label>
                        <input type="text" id="account_number" name="account_number" class="form-control"
                            placeholder="Enter bank account" />
                    </div>
                    <div class="mb-3">
                        <label for="bank_name" class="form-label">Bank Name</label>
                        <input type="text" id="bank_name" name="bank_name" class="form-control" placeholder="Enter bank name" />
                    </div>
                    <div class="mb-3">
                        <label for="account_name" class="form-label">Account Name</label>
                        <input type="text" id="account_name" name="account_name" class="form-control"
                            placeholder="Enter bank name" />
                    </div>
                </div>
            
                <!-- Cryptocurrency Fields -->
                <div id="crypto_fields" class="mt-3" style="display: none;">
                    <div class="mb-3">
                        <label for="sub_type" class="form-label">Cryptocurrency Type</label>
                        <select id="sub_type" name="sub_type" class="form-select">
                            <option value="" disabled selected>Select</option>
                            <option value="USDT">USDT</option>
                            <option value="BTC">BTC</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="wallet_address" class="form-label">Wallet Address</label>
                        <input type="text" id="wallet_address" name="wallet_address" class="form-control"
                            placeholder="Enter wallet address" />
                    </div>
                    <div class="mb-3">
                        <label for="memo" class="form-label">Memo</label>
                        <input type="text" id="memo" name="memo" class="form-control" placeholder="Enter memo (if any)" />
                    </div>
                    <div class="mb-3">
                        <label for="network_address" class="form-label">Network Address</label>
                        <input type="text" id="network_address" name="network_address" class="form-control"
                            placeholder="Enter network address" />
                    </div>
                </div>
            
                <button type="submit" class="btn btn-success mt-3">Add Payment Method</button>
            </form>

        </div>
    </div>


    <!-- Payment Method -->
    <div class="card border-0 mt-4 mb-4">
        <div class="card-header text-white shadow-sm">
            <div class="card-header bg-danger text-white" id="payments">
                <h5 class="mb-0">Payment Methods</h5>
            </div>
            <div class="card-body pl-0 pr-0">
                <!-- Make the table responsive -->
                <div class="table-responsive">
                    <table class="table table-striped">
                        <thead class="bg-primary text-white">
                            <tr>
                                <th>Method Type</th>
                                <th>Account Number</th>
                                <th>Bank Name</th>
                                <th>Account Name</th>
                                <th>Wallet Address</th>
                                <th>Memo</th>
                                <th>Network Address</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for method in payment_methods %}
                            <tr>
                                <td>{{ method.method_type }}</td>
                                <td>{{ method.account_number }}</td>
                                <td>{{ method.bank_name }}</td>
                                <td>{{ method.account_name }}</td>
                                <td>{{ method.wallet_address[:13] if method.wallet_address else '' }}</td>
                                <td>{{ method.wallet_address[:13] if method.wallet_address else '' }}</td>
                                <td>{{ method.network_address }}</td>
                                <td>
                                    <!-- Edit Button -->
                                    <button class="btn btn-sm text-success" data-bs-toggle="modal"
                                        data-bs-target="#editPaymentMethodModal" data-id="{{ method.id }}"
                                        data-user-id="{{ method.user_id }}" data-method-type="{{ method.method_type }} "
                                        data-account-number="{{ method.account_number }}"
                                        data-bank-name="{{ method.bank_name }}"
                                        data-account-name="{{ method.account_name }}" data-sub-type="{{ method.sub_type }}"
                                        data-wallet-address="{{ method.wallet_address }}" data-memo="{{ method.memo }}"
                                        data-network-address="{{ method.network_address }}">
                                        <i class="bi bi-pencil"></i> <!-- Edit Icon -->
                                    </button>
    
                                    <!-- Delete Button -->
                                    <form action="{{ url_for('accounts.delete_payment_method', method_id=method.id) }}"
                                        method="POST" style="display:inline;">
                                        <button type="submit" class="btn btn-sm text-danger">
                                            <i class="bi bi-trash"></i> <!-- Delete Icon -->
                                        </button>
                                    </form>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

    
    <!-- Edit Payment Method Modal -->
    <div class="modal fade" id="editPaymentMethodModal" tabindex="-1" aria-labelledby="editPaymentMethodModalLabel"
        aria-hidden="true">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <form action="{{ url_for('accounts.edit_payment_method') }}" method="POST">
                    <div class="modal-header">
                        <h5 class="modal-title" id="editPaymentMethodModalLabel">Edit Payment Method</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <strong>Please Don't fill all. only fill neccessery once</strong>
                        </div>
                        <input type="hidden" name="method_id" id="methodId">
                        <div class="mb-3">
                            <label for="methodType" class="form-label">Method Type</label>
                            <input type="text" class="form-control" id="methodType" name="method_type" required>
                        </div>
                        <div class="mb-3">
                            <label for="accountNumber" class="form-label">Account Number</label>
                            <input type="text" class="form-control" id="accountNumber" name="account_number">
                        </div>
                        <div class="mb-3">
                            <label for="bankName" class="form-label">Bank Name</label>
                            <input type="text" class="form-control" id="bankName" name="bank_name">
                        </div>
                        <div class="mb-3">
                            <label for="accountName" class="form-label">Account Name</label>
                            <input type="text" class="form-control" id="accountName" name="account_name">
                        </div>
                        <div class="mb-3">
                            <label for="walletAddress" class="form-label">Wallet Address</label>
                            <input type="text" class="form-control" id="walletAddress" name="wallet_address">
                        </div>
                        <div class="mb-3">
                            <label for="memo" class="form-label">Memo</label>
                            <input type="text" class="form-control" id="memo" name="memo">
                        </div>
                        <div class="mb-3">
                            <label for="networkAddress" class="form-label">Network Address</label>
                            <input type="text" class="form-control" id="networkAddress" name="network_address">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="submit" class="btn btn-primary">Save changes</button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Section 2: Users Table -->
    <div class="card shadow-sm border-0 mt-4 mb-4">
        <div class="card-header bg-success text-white" id="users">
            <h5 class="mb-0">Users</h5>
        </div>
        <div class="card-body" >
            <table class="table table-hover table-bordered mt-3 table-responsive">
                <thead class="text-white" style="background-color: #007bff;">
                    <tr>
                        <th>ID</th>
                        <th>Email</th>
                        <th>Username</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {% for user in users %}
                    <tr>
                        <td>{{ user.id }}</td>
                        <td>{{ user.email }}</td>
                        <td>{{ user.username }}</td>
                        <td>
                            <i class="bi bi-pencil text-primary me-2" style="cursor: pointer;" title="Edit"></i>
                            <i class="bi bi-chat text-success me-2" style="cursor: pointer;" title="Message"></i>
                            <i class="bi bi-trash text-danger" style="cursor: pointer;" title="Delete"></i>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
    
    <!-- Transactions Table -->
    <div class="card shadow-sm border-0 mt-4 mb-4">
        <div class="card-header text-white" style="background-color: #6c757d;" id="transactions">
            <h5 class="mb-0">Transactions</h5>
        </div>
        <div class="card-body" >
            <table class="table table-hover table-bordered mt-3">
                <thead class="text-white bg-primary">
                    <tr>
                        <th>ID</th>
                        <th>Username</th>
                        <th>Amount</th>
                        <th>Status</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {% for transaction in transactions %}
                    <tr>
                        <td>{{ transaction.id }}</td>
                        <td>{{ transaction.user.username }}</td>
                        <td>PGK {{ transaction.amount }}</td>
                        <td>
                            {% if transaction.transaction_status == 'Completed' %}
                            <span class="badge bg-success text-white">Completed</span>
                            {% else %}
                            <span class="badge bg-warning text-dark">Pending</span>
                            {% endif %}
                        </td>
                        <td>
                            <!-- Modal Trigger Button -->
                            <button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#editModal" onclick="populateModal('{{ transaction.user.id }}', '{{ transaction.id }}', '{{ transaction.user.acc_balance }}', 
                                                                   '{{ transaction.user.total_investment }}', '{{ transaction.user.monthly_return }}', 
                                                                   '{{ transaction.transaction_status }}')">
                                <i class="bi bi-pencil text-primary"></i> <!-- Edit Icon -->
                            </button>
                            <!-- Delete Button -->
                            <form method="POST" action="{{ url_for('accounts.delete_transaction', transaction_id=transaction.id) }}" style="display:inline;">
                                <button type="submit" class="btn"
                                    onclick="return confirm('Are you sure you want to delete this transaction?')">
                                    <i class="bi bi-trash text-danger"></i> <!-- Trash Icon -->
                                </button>
                            </form>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
    
    <!-- Edit Transaction Modal -->
    <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="editModalLabel">Edit Transaction</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form method="POST" action="{{ url_for('accounts.edit_transaction') }}">
                        <!-- Hidden input for user_id -->
                        <input type="hidden" name="user_id" id="user_id" value="">
                        <!-- Hidden input for transaction_id -->
                        <input type="hidden" name="transaction_id" id="transaction_id" value="">
    
                        <!-- User Data Fields -->
                        <div class="mb-3">
                            <label for="acc_balance" class="form-label">Account Balance</label>
                            <input type="number" step="0.01" class="form-control" id="acc_balance" name="acc_balance">
                        </div>
                        <div class="mb-3">
                            <label for="total_investment" class="form-label">Total Investment</label>
                            <input type="number" step="0.01" class="form-control" id="total_investment"
                                name="total_investment">
                        </div>
                        <div class="mb-3">
                            <label for="monthly_return" class="form-label">Monthly Return</label>
                            <input type="number" step="0.01" class="form-control" id="monthly_return" name="monthly_return">
                        </div>
    
                        <!-- Transaction Status Field -->
                        <div class="mb-3">
                            <label for="transaction_status" class="form-label">Transaction Status</label>
                            <select class="form-select" id="transaction_status" name="transaction_status">
                                <option value="Pending">Pending</option>
                                <option value="Completed">Completed</option>
                            </select>
                        </div>
    
                        <button type="submit" class="btn btn-primary">Save Changes</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
    
</div>

<script>
    function toggleMethodFields() {
        const methodType = document.getElementById('method_type').value;
        document.getElementById('bank_fields').style.display = methodType === 'Bank Transfer' ? 'block' : 'none';
        document.getElementById('crypto_fields').style.display = methodType === 'Cryptocurrency' ? 'block' : 'none';
    }

    document.addEventListener("DOMContentLoaded", function () {
        const editModal = document.getElementById('editPaymentMethodModal');

        editModal.addEventListener('show.bs.modal', function (event) {
            // Button that triggered the modal
            const button = event.relatedTarget;

            // Extract data attributes from the button
            const methodId = button.getAttribute('data-id');
            const userId = button.getAttribute('data-user-id');
            const methodType = button.getAttribute('data-method-type');
            const accountNumber = button.getAttribute('data-account-number');
            const bankName = button.getAttribute('data-bank-name');
            const accountName = button.getAttribute('data-account-name');
            const subType = button.getAttribute('data-sub-type');
            const walletAddress = button.getAttribute('data-wallet-address');
            const memo = button.getAttribute('data-memo');
            const networkAddress = button.getAttribute('data-network-address');

            // Update modal fields
            editModal.querySelector('#methodId').value = methodId;
            editModal.querySelector('#methodType').value = methodType || '';
            editModal.querySelector('#accountNumber').value = accountNumber || '';
            editModal.querySelector('#bankName').value = bankName || '';
            editModal.querySelector('#accountName').value = accountName || '';
            editModal.querySelector('#walletAddress').value = walletAddress || '';
            editModal.querySelector('#memo').value = memo || '';
            editModal.querySelector('#networkAddress').value = networkAddress || '';
        });
    });

   


    function populateModal(userId, transactionId) {
        fetch(`/accounts/get_user/${userId}`)
            .then(response => response.json())
            .then(data => {
                // Populate user information
                document.getElementById('userId').value = data.id;

                // Find the specific transaction
                const transaction = data.transactions.find(tx => tx.id === transactionId);
                if (transaction) {
                    document.getElementById('transaction_id').value = transaction.id;
                    document.getElementById('transaction_status').value = transaction.transaction_status;
                }
            });
    }


    

    function populateModal(userId, transactionId, accBalance, totalInvestment, monthlyReturn, transactionStatus) {
        // Set the user_id and transaction_id dynamically when the button is clicked
        document.getElementById('user_id').value = userId;
        document.getElementById('transaction_id').value = transactionId;

        // Set the user fields in the modal
        document.getElementById('acc_balance').value = accBalance;
        document.getElementById('total_investment').value = totalInvestment;
        document.getElementById('monthly_return').value = monthlyReturn;

        // Set the transaction status field in the modal
        document.getElementById('transaction_status').value = transactionStatus;
    }

</script>



{% endblock %}
