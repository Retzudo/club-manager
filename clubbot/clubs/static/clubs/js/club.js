Vue.http.headers.common['X-CSRFToken'] = getCookie('csrftoken');

Vue.component('cash-table', {
    props: ['clubId'],
    data: function () {
        return {
            cash: null,
            transactions: []
        };
    },

    mounted: function () {
        var that = this;
        this.$http.get('/api/v1/clubs/' + this.clubId + '/cash')
        .then(function (response) {
            return response.json();
        }).then(function (data) {
            that.cash = data;
        });

        this.$http.get('/api/v1/clubs/' + this.clubId + '/cash/transactions')
        .then(function (response) {
            return response.json();
        }).then(function (data) {
            that.transactions = data;
        });
    },

    methods: {
        negative: function (number) {
            return number * -1;
        },
        format: function (number) {
            return number.toFixed(2);
        },
        humanDate: function (dateString) {
            return moment.utc(dateString).fromNow();
        }
    }
});

Vue.component('delete-club-modal', {
    props: ['clubId'],

    methods: {
        deleteClub: function () {
            var that = this;
            this.$http.delete('/api/v1/clubs/' + that.clubId + '/')
            .then(function (response) {
                $(that.$el).modal('hide');
                if (response.ok && response.status === 204) {
                    window.location = '/account';
                }
            });
        }
    }
});

new Vue({
    el: '#club-app'
});