module.exports = {
    entry: './static/src/js/main.js',
    output: {
        path: './static/dist/',
        publicPath: '/static',
        filename: 'main.js'
    },
    module: {
        loaders: [
            {
                test: /\.js/,
                exclude: /node_modules/,
                loader: 'babel',
                query: {
                    presets: ['es2015']
                }
            }
        ]
    }
};