import sys
input = sys.stdin.readline

class AlbumTree:
    def __init__(self, album_name, super_album):
        self.album_name = album_name
        self.super_album = super_album
        self.sub_albums = set()
        self.sub_album_names = set()
        self.images = set()

    def __gt__(self, other):
        return self.album_name > other.album_name

class AlbumManager:
    def __init__(self):
        self.root = AlbumTree('album', None)
        self.cur = self.root

    def create_album(self, album_name):
        cur = self.cur
        if album_name in cur.sub_album_names:
            return 'duplicated album name\n'
        else:
            cur.sub_albums.add(AlbumTree(album_name, cur))
            cur.sub_album_names.add(album_name)
            return ''

    def delete_album(self, instance):
        cur = self.cur
        if instance == '0':
            album_cnt = len(cur.sub_albums)
            image_cnt = 0
            for album in cur.sub_albums:
                a_cnt, i_cnt = self.delete_sub_album(album)
                album_cnt += a_cnt
                image_cnt += i_cnt
            cur.sub_albums.clear()
            cur.sub_album_names.clear()
        elif instance == '1' or instance == '-1':
            if not cur.sub_albums:
                return 0, 0
            if instance == '1':
                album = max(cur.sub_albums)
            else:
                album = min(cur.sub_albums)
            album_cnt, image_cnt = self.delete_sub_album(album)
            album_cnt += 1
            cur.sub_album_names.remove(album.album_name)
            cur.sub_albums.remove(album)
        else:
            for sub_album in cur.sub_albums:
                if sub_album.album_name == instance:
                    album = sub_album
                    break
            else:
                return 0, 0
            album_cnt, image_cnt = self.delete_sub_album(album)
            album_cnt += 1
            cur.sub_album_names.remove(album.album_name)
            cur.sub_albums.remove(album)

        return album_cnt, image_cnt

    def delete_sub_album(self, cur_album:AlbumTree):
        album_cnt, image_cnt = len(cur_album.sub_albums), len(cur_album.images)
        for nxt_album in cur_album.sub_albums:
            a_cnt, i_cnt = self.delete_sub_album(nxt_album)
            album_cnt += a_cnt
            image_cnt += i_cnt
        return album_cnt, image_cnt

    def insert_image(self, image_name):
        cur = self.cur
        if image_name in cur.images:
            return 'duplicated photo name\n'
        else:
            cur.images.add(image_name)
            return ''

    def delete_image(self, instance):
        cur = self.cur
        if instance == '0':
            image_cnt = len(cur.images)
            cur.images.clear()
        else:
            image_cnt = 1
            image = instance
            if instance == '1' and cur.images:
                image = max(cur.images)
            elif instance == '-1' and cur.images:
                image = min(cur.images)
            elif instance not in cur.images:
                return 0
            cur.images.remove(image)
        return image_cnt

    def goto(self, instance):
        cur = self.cur
        if instance == '..' and cur.album_name != 'album':
            self.cur = cur.super_album
        elif instance == '/':
            self.cur = self.root
        else:
            for sub_album in cur.sub_albums:
                if sub_album.album_name == instance:
                    self.cur = sub_album
        return self.cur.album_name

def main():
    manager = AlbumManager()
    n = int(input())
    responses = []
    for _ in range(n):
        command, instance = input().split()
        if command == 'mkalb':
            response = manager.create_album(instance)
            responses.append(response)
        elif command == 'rmalb':
            response = manager.delete_album(instance)
            responses.append(f"{response[0]} {response[1]}\n")
        elif command == 'insert':
            response = manager.insert_image(instance)
            responses.append(response)
        elif command == 'delete':
            response = manager.delete_image(instance)
            responses.append(f"{response}\n")
        elif command == 'ca':
            response = manager.goto(instance)
            responses.append(f"{response}\n")
    print(''.join(responses))

if __name__ == "__main__":
    main()