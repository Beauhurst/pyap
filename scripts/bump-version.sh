#!/bin/sh
set -x -e

# This defines the canonical way of bumping version
case "$PRE_RELEASE" in
true | 1)
    echo "Bumping version for pre-release"
    CURRENT_VERSION="$(uvx --from toml-cli toml get --toml-path pyproject.toml project.version)"
    case "$CURRENT_VERSION" in
    *dev*)
        #2024.9.1-dev0 -> #2024.9.1-dev1
        uvx --from bump-my-version bump-my-version bump pre_release
        ;;
    *)
        #2024.9.0 -> #2024.9.1-dev0
        uvx --from bump-my-version bump-my-version bump num
        ;;
    esac
    ;;
*)
    echo "Bumping version for release"

    # find if we can bump just the label
    # this will fail when pre_label bumping cannot be done (i.e. it's already stable)
    # this will succeed but include dev it if is bumping the calver section
    POTENTIAL_NEW_VERSION="$(uvx --from bump-my-version bump-my-version show -i pre_label new_version 2>/dev/null || echo 'error')"
    case "$POTENTIAL_NEW_VERSION" in
    error | *dev*)
        #2024.9.0 -> #2024.9.1
        uvx --from bump-my-version bump-my-version bump num --no-commit --no-tag
        uvx --from bump-my-version bump-my-version bump pre_label --allow-dirty
        ;;
    *)
        #2024.9.1-dev0 -> #2024.9.1
        uvx --from bump-my-version bump-my-version bump pre_label
        ;;
    esac
    ;;
esac

NEW_VERSION="$(uvx --from toml-cli toml get --toml-path pyproject.toml project.version)"

echo "$NEW_VERSION"
