# Twitter API Setup Guide

This guide will help you properly set up your Twitter Developer account and app for the tweet deletion tool.

## 1. Twitter Developer Account Setup

1. Go to [Twitter Developer Portal](https://developer.twitter.com)
2. Sign in with your Twitter account
3. Create a new project or use an existing one
4. Create a new app within your project

## 2. App Permissions

For tweet deletion, you **must** set your app permissions to **"Read and write"**:

1. In your app settings, find "User authentication settings"
2. Under "App permissions", select **"Read and write"**
3. Save changes

![App Permissions](https://docs.x.com/fundamentals/developer-apps#app-permissions)

## 3. Authentication Type

For our tweet deletion tool, we need **OAuth 1.0a** authentication:

1. Select the appropriate app type:
   - "Native App" (if running as a desktop app)
   - "Web App, Automated App or Bot" (if running as a script)

2. Make sure "OAuth 1.0a" is enabled in your app settings

## 4. App Information

Fill in required fields in your app settings:

- **Callback URL / Redirect URL**: `http://127.0.0.1` (for local testing)
- **Website URL**: Your website or GitHub repo URL
- **Organization name**: Your name or organization
- **Organization URL**: Your website URL

Optional fields (only required for some API access levels):
- **Terms of service URL**
- **Privacy policy URL**

## 5. Generate API Keys and Tokens

After setting permissions, you need to generate new keys and tokens:

1. Go to "Keys and tokens" tab
2. Generate (or regenerate) your:
   - API Key and Secret (also called Consumer Key and Secret)
   - Access Token and Secret
   - Bearer Token (optional, used for read operations)

3. Copy these values immediately - you won't be able to see them again!

## 6. Update .env File

Update your `.env` file with the new credentials:

```
TWITTER_CONSUMER_KEY=your_api_key
TWITTER_CONSUMER_SECRET=your_api_key_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
TWITTER_BEARER_TOKEN=your_bearer_token
```

## Troubleshooting

If you see "Your client app is not configured with the appropriate oauth1 app permissions for this endpoint":

1. Make sure your app has "Read and write" permissions
2. Regenerate your Access Token and Secret after changing permissions
3. Update your `.env` file with the new tokens

## References

- [Twitter Authentication Mapping Guide](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [Twitter App Permissions Documentation](https://docs.x.com/fundamentals/developer-apps#app-permissions)
