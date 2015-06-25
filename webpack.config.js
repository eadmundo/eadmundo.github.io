var path = require('path');
var webpack = require('webpack');

var ExtractTextPlugin = require('extract-text-webpack-plugin');
var ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');
var Clean = require('clean-webpack-plugin');

var rootAssetPath = './static';
var outputFolder = './build/public';

module.exports = {
    entry: {
        styles: [
            rootAssetPath + '/css/main.css'
        ]
    },
    output: {
        path: outputFolder,
        publicPath: '/public/',
        filename: '[name].[hash].js'
    },
    resolve: {
        extensions: ['', '.js', '.css']
    },
    module: {
        noParse: [
          /\.DS_Store$/
        ],
        loaders: [
            {
                test: /\.css$/i,
                loader: ExtractTextPlugin.extract('style-loader', 'css-loader')
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin('[name].[hash].css'),
        new ManifestRevisionPlugin(path.join('build', 'manifest.json'), {
            rootAssetPath: rootAssetPath,
            ignorePaths: ['/css']
        }),
        new Clean([outputFolder])
    ]
};
