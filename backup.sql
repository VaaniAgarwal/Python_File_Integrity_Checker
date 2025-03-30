PGDMP      *                }            file_integrity_checker    17rc1    17rc1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    24585    file_integrity_checker    DATABASE     �   CREATE DATABASE file_integrity_checker WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_India.1252';
 &   DROP DATABASE file_integrity_checker;
                     postgres    false            �           0    0    DATABASE file_integrity_checker    ACL     <   GRANT ALL ON DATABASE file_integrity_checker TO flask_user;
                        postgres    false    4851            �            1259    24587    file_hashes    TABLE     �   CREATE TABLE public.file_hashes (
    id integer NOT NULL,
    filename text NOT NULL,
    file_hash text NOT NULL,
    uploaded_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.file_hashes;
       public         heap r    
   flask_user    false            �            1259    24586    file_hashes_id_seq    SEQUENCE     �   CREATE SEQUENCE public.file_hashes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.file_hashes_id_seq;
       public            
   flask_user    false    218            �           0    0    file_hashes_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.file_hashes_id_seq OWNED BY public.file_hashes.id;
          public            
   flask_user    false    217            W           2604    24590    file_hashes id    DEFAULT     p   ALTER TABLE ONLY public.file_hashes ALTER COLUMN id SET DEFAULT nextval('public.file_hashes_id_seq'::regclass);
 =   ALTER TABLE public.file_hashes ALTER COLUMN id DROP DEFAULT;
       public            
   flask_user    false    217    218    218            �          0    24587    file_hashes 
   TABLE DATA           K   COPY public.file_hashes (id, filename, file_hash, uploaded_at) FROM stdin;
    public            
   flask_user    false    218   `       �           0    0    file_hashes_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.file_hashes_id_seq', 11, true);
          public            
   flask_user    false    217            Z           2606    24595    file_hashes file_hashes_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.file_hashes
    ADD CONSTRAINT file_hashes_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.file_hashes DROP CONSTRAINT file_hashes_pkey;
       public              
   flask_user    false    218            �   i   x�ȱ� ����>BƝ�i�wis?�׽�����{�i�+L+&vMצTIGo�1��d��'����������˻c�$xc��(rR��?)����     